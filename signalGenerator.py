import numpy as np
import preampSignalGenerator
import matplotlib.pyplot as plt
def isEvent(i,start,stop,activity):
    howManyEvents=(stop-start)*activity/(100000000)
    
    x=np.random.randint(int(stop-start))
    if howManyEvents>x:
        return True
    else :
        return False
#activity in becqureles 1/s
activity=50000
halfLife=500
start=0
stop=15000
amplitude=100
decayTime=1500
riseTime=200
startTimes=[]
signal=0
signals=[]
times=[]
for i in range(start,stop):
    signal=0
    if isEvent(i,start,stop,activity):
        startTimes.append(i)
    
    if len(startTimes)>0:
        for startTime in startTimes:
            signal+=preampSignalGenerator.preampSignal(startTime,amplitude,i,riseTime,decayTime)
    else: 
        signal=0
    signals.append(signal)
    times.append(i)
    if len(startTimes)>0 and i+1-startTimes[0]>5*decayTime:
        del startTimes[0]

signals=np.array(signals)
times=np.array(times)
plt.plot(times,signals)
plt.show()
