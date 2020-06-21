import csv

import serial
import time
ser = serial.Serial('COM9', 9600, timeout=0)

time_data = list()
user_data = list()
while (len(time_data)<6):
    value = str(ser.readline())
    print(value)
    time_ID = (value[2:4])
    print("TYPE:", time_ID)
    value = (value[4:][:-5])
    print("VALUE:", value)
    if time_ID == "u-":
        user_data.append(value)
    if time_ID == "t-":
        time_data.append(value)
    time.sleep(.5)


with open('DonutData.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'timeStamp']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for count in range(len(time_data)):
        writer.writerow({'id': user_data[count], 'timeStamp': time_data[count]})