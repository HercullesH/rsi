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

arq = open('dados.txt','r')

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
                    if js['coords']['speed'] > 0:
                        passageiro.setLastLatitude(js['coords']['latitude'])
                        passageiro.setLastLongitude(js['coords']['longitude'])
                        passageiro.setSpeed(js['coords']['speed'])

                        if rssi >= -90:

                            # decaimento gradual do sinal RSSI - OBSERVAÇÃO, QUAL DEVE SER O PARÂMETRO DE DECAIMENTO?? ARTÍGO NÃO ESPECIFÍCA
                            #UTILIZEI DECAIMENTO DE 37 NO SINAL - PERGUNTAR A GLAUCO

                            if (rssi + 37) < passageiro.getRssi():
                                #nao é um passageiro
                                break
                            else:
                                passageiro.setSituacao(True) 
                    
                    else:
                        #provavel pedestre
                        # Setando o objeto para tentar melhorar  a precisão do algorítmo
                        if passageiro.getSpeed() == -1:
                            passageiro.setSituacao(False)
                        else:    
                            passageiro.setSpeed(-1)
                        break
                    break


                else:
                    # diferença de probe menor que um segundo
                    break
                
        if cont == 0:    
            novoPassageiro = Passageiro()
            novoPassageiro.setMac(mac)
            novoPassageiro.setRssi(rssi)
            novoPassageiro.setLastTime(tratarMoment(linha[0]))
            novoPassageiro.setCurrentTime(tratarMoment(linha[0]))
            novoPassageiro.setFirstTime(tratarMoment(linha[0]))
            novoPassageiro.setFirstLatitude(js['coords']['latitude'])
            novoPassageiro.setFirstLongitude(js['coords']['longitude'])
            novoPassageiro.setLastLatitude(js['coords']['latitude'])
            novoPassageiro.setLastLongitude(js['coords']['longitude'])
            novoPassageiro.setSpeed(js['coords']['speed'])
            passageiros.append(novoPassageiro)
    
    else:
        novoPassageiro = Passageiro()
        novoPassageiro.setMac(mac)
        novoPassageiro.setRssi(rssi)
        novoPassageiro.setLastTime(tratarMoment(linha[0]))
        novoPassageiro.setCurrentTime(tratarMoment(linha[0]))
        novoPassageiro.setFirstTime(tratarMoment(linha[0]))
        novoPassageiro.setFirstLatitude(js['coords']['latitude'])
        novoPassageiro.setFirstLongitude(js['coords']['longitude'])
        novoPassageiro.setLastLatitude(js['coords']['latitude'])
        novoPassageiro.setLastLongitude(js['coords']['longitude'])
        novoPassageiro.setSpeed(js['coords']['speed'])
        passageiros.append(novoPassageiro)


#


for k in passageiros:

    j = k.getFirstTime() - k.getLastTime()
    j = j.total_seconds() / 60
    
    #tempo total presente no ônibus em minutos
    print( j )

    print('-------------------')

#Total de probes diferentes analizados  , não de passageiros . tempo total presente no ônibus pequenos devem ser retirados
print(len(passageiros))