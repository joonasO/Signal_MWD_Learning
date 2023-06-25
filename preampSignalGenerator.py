import  numpy as np
def risePart(riseTime,amplitude,time):
    constant=amplitude/riseTime
    return constant*time

def decayPart(amplitude,decayTime,riseTime,time):
    timeAtDecayCurve=time-riseTime
    decayValue=timeAtDecayCurve/decayTime
    return amplitude*np.exp(-decayValue)
# Decay time in 10 ns scale
# Rise time in 10 ns 
def preampSignal(startTime,amplitude,currentTime,riseTime=200,decayTime=1500):
    timePreamSignal=currentTime-startTime
    if timePreamSignal<=riseTime:
        return risePart(riseTime,amplitude,timePreamSignal)
    else:
        return decayPart(amplitude,decayTime,riseTime,timePreamSignal)