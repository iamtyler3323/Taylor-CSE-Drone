import random
most_recent = []
target = 2
throttle = 1500
DOWN = "DOWN"
UP = "UP"

def average():
    result = 0
    for i in most_recent:
        print("{}".format(i))
        result += i

    result = result/len(most_recent)
    return result

def averageSoFar(start, stop):
    result = float(0)
    count = 0
    for i in range(start,stop):
        #print("\tAVG: {0}".format(most_recent[i]))
        result += most_recent[i]
        count += 1
    return result/count

def trending():
    up_count = 0
    down_count = 0
    if len(most_recent) < 1:
        return "BROKE"
    previous = most_recent[0]
    for i in most_recent:
        if i > previous:
            up_count += 1
        elif i < previous:
            down_count += 1
        previous = i
    if up_count > down_count:
        return UP
    elif down_count > up_count:
        return DOWN
    else:
        return "NORMAL"

def correction(start, stop):
    print("In correction")
    current = averageSoFar(start,stop)
    print("Got current")
    trend = trending()
    print("Got trend")
    global throttle
    if trend is DOWN and current < target:
        print("Should be corrected by {0}".format(target-current))
        throttle += (target - current)
    elif trend is DOWN and current > target:
        print("Still descending, keep here")

    elif trend is "NORMAL" and current == target:
        print("We are on target")

    elif trend is UP and current < target:
        print("Still rising, keep throttle here")

    elif trend is UP and current > target:
        print("Trending up, correct by {0}".format((target-current)))
        throttle += (target-current)
        
    print("Throttle: {0}".format(throttle))

runs = 0
data = [[1.7, 1.7, 1.69, 1.69, 1.69, 1.67, 1.67, 1.67, 1.67, 1.67],[1.67, 1.67, 1.67, 1.67, 1.65, 1.64, 1.64, 1.64, 1.64, 1.63],[1.63, 1.63, 1.63, 1.63, 1.64, 1.64, 1.64, 1.64, 1.64, 1.64],[1.64, 1.64, 1.64, 1.64, 1.64, 1.64, 1.63, 1.61, 1.61, 1.61],[1.59, 1.59, 1.59, 1.58, 1.56, 1.56, 1.56, 1.56, 1.56, 0.01],[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.76, 0.93],[0.93, 1.05, 1.05, 1.15, 1.15, 1.15, 1.15, 1.18, 1.18, 1.18],[1.18, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.18, 1.18]]

## TEST FUNCTIONALITY WITH RANDOMIZED DATA ##
#for i in range(0,len(data)):
#    print("Run {}".format(i))
#    most_recent = data[i]
#    correction(0,10)
#    print(trending())
#    print(most_recent)
#    print(i)

## UNCOMMENT FOR REAL FLIGHTS ##     
for chan in range(1,9):
    Script.SendRC(chan,1500,False)
Script.SendRC(3,Script.GetParam('RC3_MIN'),True)

Script.Sleep(4000)
if cs.lat != 0:
    print('We got a  GPS signal!')
print('Lowering throttle voltage')
Script.SendRC(3,1000,False)
Script.SendRC(4,2000,True)
cs.messages.Clear()
print('Waiting for motors to be armed...')
Script.WaitFor('ARMING MOTORS', 5000)
print('Motors armed.')

ground_alt = cs.alt
target_altitude = ground_alt + 2
print('Ground alt: {0} | Target alt: {1}'.format(ground_alt,target_altitude))

#Setting yaw to not turn
Script.SendRC(4,1500,True) # 1000 - turn left 2000 - turn right
#liftoff
print('Lifting off')
Script.SendRC(3,1500,True)

while cs.sonarrange < target_altitude:
    Script.Sleep(50)
    Script.SendRC(3,1370,True)


Script.SendRC(5,1500,False) # stabilize

while runs < 30:
    print("Run {0}".format(runs))
    runs += 1
    alt = cs.sonarrange
    if alt > 3:
	alt = cs.alt
    most_recent.append(alt)
    for i in range(0,11):
	alt = cs.sonarrange
	if alt > 3:
	    alt = cs.alt
	most_recent.append(alt)
	Script.Sleep(100)
    Script.Sleep(100)
    correction(0,11)
    print("\tAverage: {0} Trending: {1} ".format(average(),trending()))
    print("Throttle: {0}".format(throttle))
    Script.SendRC(3,throttle,True)
    if len(most_recent) > 10:
        for i in range(0,len(most_recent)):
            most_recent.pop()
            print("\t{0}".format(most_recent))
    print("cs.alt: {0} | cs.sonarrange: {1}".format(alt,cs.sonarrange))

print('Descending...')
for i in range(3,15):
    Script.SendRC(3,1530-(i*1),True)
    Script.Sleep(50)
    if cs.alt <= ground_alt+0.1:
        break
Script.SendRC(3,1515,True)
while cs.alt > ground_alt+0.1:
    Script.Sleep(50)
    print('Descent at: {0}'.format(cs.alt))

Script.SendRC(3,1000,False)
Script.SendRC(4,1000,True)
Script.WaitFor('DISARMING MOTORS',30000)
Script.SendRC(4,1500,True)
