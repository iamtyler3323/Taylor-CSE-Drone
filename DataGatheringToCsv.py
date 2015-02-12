import csv
import os
import os.path
import platform

target_data_count = 10;
def get():
    return cs.alt


userhome = os.path.expanduser('~')
#change user to yourself, or if on personal Windows computer use desktop = userhome+"Desktop/"
desktop = "//fileshare/tgarcia/Desktop/"
count = 0

#Change to what you want your file to be called, otherwise you will append to whatever is here
file_name = desktop + 'dataTestAlt.csv'
print(file_name +"Exists? " + str(os.path.exists(file_name)))
if os.path.isfile(file_name):
    print("File exists")
    with open(file_name,'rb') as f:
        data = list(csv.reader(f))
else:
    print("Making new file")
    f = open(file_name,'w')
    with open(file_name,'rb') as f:
        data = list(csv.reader(f))

f = open(file_name,"wb")
import collections
counter = collections.defaultdict(int)
for row in data:
    counter[row[0]] += 1

writer = csv.writer(f)
while count < target_data_count:
    count += 1
    writer.writerow(["{0}".format(get())])
    #print("{0}\t{1}".format(get(),count))
    Script.Sleep(100)
                    
f.close()
