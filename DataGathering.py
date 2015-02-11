def target_param():
    return cs.sonarrange
target_data_count = 500
target_timer = 5000 #milliseconds
count = 0

for chan in range(1,9):
    Script.SendRC(chan,1500,False)

while target_timer > 0 or count < target_data_count:
    target_timer = target_timer-100
    Script.Sleep(100)
    count = count + 1
    print("{0}\t{1}".format(count,target_param()))
