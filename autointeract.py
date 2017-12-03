import numpy as np
import webbrowser
import random

def dateRandomizer(month):
    if month == 2:
        daysLi = range(1,29)
    elif month == 11:
        daysLi = range(1,18)+range(26,31)
    else:
        daysLi = range(1,30)
    day = random.choice(daysLi)

    if day in range(1,10):
        day = "0"+str(day)
    else:
        day = str(day)

    if month in range(1,10):
        month = "0"+str(month)
    else:
        month = str(month)
    #=2017-11-02&entry

    formDate = "=2017-"+month+"-"+day+"&entry"
    return formDate


my_data = np.genfromtxt('rosterwithinterlinks.txt', dtype=np.str, delimiter='\t')

urls = my_data[:,12]
floors = my_data[:,6].astype(np.int)
building = my_data[:,2]

print my_data[0,12]

print building

while True:
    inpBuiling = raw_input('Enter your building (Hamlin/Leach): ').lower()

    if inpBuiling  in ["hamlin", "leach"] :
        break
    elif inpBuiling == "leech":
        print "It's spelled Leach... but I'll take this"
        inpBuiling="leach"
        break
    else:
        print "Incorrect building"

while True:
    inpFloor = input('Enter your floor (1,2,3,4): ')
    if inpFloor < 1 or inpFloor > 4:
        print "Incorrect floor number"
    else:
        break

while True:
    inpMon = input('Enter month of interactions in numerical format (1 to 12): ')
    if isinstance(inpMon,int) == False:
        print "Not a number"
    elif inpMon < 0 or inpMon > 12:
        print "Invalid date"
    else:
        break

li=[]
for i in range(my_data.shape[0]):
    if (building[i].lower()==inpBuiling) and (floors[i]==inpFloor):
        li.append(my_data[i,12].replace('"', '').replace('=2017-11-02&entry',dateRandomizer(inpMon)))
print li
print ""
print li[0]
for x in range(len(li)):
    webbrowser.open(li[1])
