import json
import datetime
from passageiro import *

def tratarMoment(moment):
    moment = str(moment)
    parte1 = moment[0:10:]
    parte2 = moment[10:13:]
    moment = parte1+'.'+parte2
    moment = float(moment)
    moment = datetime.datetime.fromtimestamp(moment)
    return moment

arq = open('probes.txt','r')

dados = arq.readlines()

arq.close()
passageiros = []

for num,linha in enumerate(dados,start=0):

    if(num % 2 != 0):
        continue
        
    linha = linha.split('#')
    if len(linha) <= 2:
        continue
    linha[0] = linha[0].replace(' ','').split(':')
    linha[0] = linha[0][1]
    linha[1] = linha[1].replace(' ','')

    js = json.loads(linha[1])

    linha[2] = linha[2].replace('RSSI:','#')
    linha[2] = linha[2].replace('Ch:','#')
    linha[2] = linha[2].replace('Peer MAC:','#')
    linha[2] = linha[2].replace('SEQ:','#')
    linha[2] = linha[2].replace(" ","").split('#')
    if num % 2 == 0 and len(linha[2]) <2:
        continue
    rssi = linha[2][1]
    mac = linha[2][3]
    #print("rsi: "+ rssi + " mac: " + mac)
    cont = 0
    if len(passageiros) > 0:
        for i,passageiro in enumerate(passageiros,start=0):
            
            if passageiro.getMac() == mac:
                cont += 1

                diferenca = tratarMoment(linha[0]) - passageiro.getLastTime()

                if diferenca.total_seconds() > 1:

                    passageiro.setLastTime(tratarMoment(linha[0]))
                    #BUS IS MOVING - QUAL DEVE SER A VELOCIDADE PARA UTILIZAR PARA  O ONIBUS SE MOVENDO? APENAS != 0? ARTIGO NÃO ESPECIFÍCA
                    #if js['coords']['speed'] > 0:
                    if js['coords']['latitude'] != passageiro.getLastLatitude or js['coords']['longitude'] != passageiro.getLastLongitude:

                        #print('ola')
                        passageiro.setLastLatitude(js['coords']['latitude'])
                        passageiro.setLastLongitude(js['coords']['longitude'])
                        #passageiro.setNegativo(js['coords']['speed'])

                        if float(rssi) >= -90:

                            if  float(rssi) < float(passageiro.getLastRssi()):
                                if float(passageiro.getLastRssi()) < float(passageiro.getRssi()):
                                    passageiro.setNegativo(passageiro.getNegativo() + 1)

                                passageiro.setRssi(passageiro.getLastRssi())
                                passageiro.setLastRssi(float(rssi))
                                break
                            else:
                                passageiro.setPositivo(passageiro.getPositivo() + 1) 

                            passageiro.setRssi(passageiro.getLastRssi())
                            passageiro.setLastRssi(float(rssi))
                    
                    else:
                        passageiro.setNegativo(passageiro.getNegativo() + 1)
                    break


                else:
                    # diferença de probe menor que um segundo
                    break
                
        if cont == 0:    
            novoPassageiro = Passageiro()
            novoPassageiro.setMac(mac)
            novoPassageiro.setRssi(rssi)
            novoPassageiro.setLastRssi(rssi)
            novoPassageiro.setLastTime(tratarMoment(linha[0]))
            novoPassageiro.setCurrentTime(tratarMoment(linha[0]))
            novoPassageiro.setFirstTime(tratarMoment(linha[0]))
            novoPassageiro.setFirstLatitude(js['coords']['latitude'])
            novoPassageiro.setFirstLongitude(js['coords']['longitude'])
            novoPassageiro.setLastLatitude(js['coords']['latitude'])
            novoPassageiro.setLastLongitude(js['coords']['longitude'])
            novoPassageiro.setNegativo(0)
            novoPassageiro.setPositivo(0)
            passageiros.append(novoPassageiro)
    
    else:
        novoPassageiro = Passageiro()
        novoPassageiro.setMac(mac)
        novoPassageiro.setRssi(rssi)
        novoPassageiro.setLastRssi(rssi)
        novoPassageiro.setLastTime(tratarMoment(linha[0]))
        novoPassageiro.setCurrentTime(tratarMoment(linha[0]))
        novoPassageiro.setFirstTime(tratarMoment(linha[0]))
        novoPassageiro.setFirstLatitude(js['coords']['latitude'])
        novoPassageiro.setFirstLongitude(js['coords']['longitude'])
        novoPassageiro.setLastLatitude(js['coords']['latitude'])
        novoPassageiro.setLastLongitude(js['coords']['longitude'])
        novoPassageiro.setNegativo(0)
        novoPassageiro.setPositivo(0)
        passageiros.append(novoPassageiro)


#

cont = 0;
for k in passageiros:

    j = k.getLastTime() - k.getFirstTime()
    j = j.total_seconds() / 60
    
    #tempo total presente no ônibus em minutos

    if k.getPositivo() > 2:
        cont +=1
        print("passanger "+ str(cont)+": "+ str(j))

print(cont)


#Total de probes diferentes analizados  , não de passageiros . tempo total presente no ônibus pequenos devem ser retirados