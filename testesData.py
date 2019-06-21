import datetime

timestamp1 = datetime.datetime.fromtimestamp(1559696015.881)
print(timestamp1.strftime('%Y-%m-%d %H:%M:%S'))

timestamp2 = datetime.datetime.fromtimestamp(1559696607.345)
print(timestamp2.strftime('%Y-%m-%d %H:%M:%S'))



'''def tratarMoment(moment):
    moment = str(moment)
    parte1 = moment[0:10:]
    parte2 = moment[10:13:]
    moment = parte1+'.'+parte2
    moment = float(moment)
    moment = datetime.datetime.fromtimestamp(moment)
    return moment

moment = tratarMoment(1559696298785)
print(moment.strftime('%Y-%m-%d %H:%M:%S'))'''