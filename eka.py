import datetime
import csv

vehicle_no = []
vehicle_type = []
parking =[]
vehicle ={}
entered = False
exited = False
entry_time = ""
exit_time = ""
with open('log.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        date_time = row[0]
        vehicle_no = row[1]
        vehicle_type =row[2]
        parking = row[3]
        if vehicle_no not in vehicle.keys():
            entry_time = ""
            exit_time = ""
        if parking == "Entry":
            entry_time = date_time
        elif parking == "Exit":
            exit_time = date_time
        vehicle[vehicle_no] = [vehicle_type,entry_time,exit_time]
        #print(date_time)
        #print(date)
        #print(time)
        #print(vehicle)
    for key in vehicle.keys():
        if vehicle[key][1] != "" and vehicle[key][2] != "":
            entry_date = vehicle[key][1].split(" ")[0].split("-")
            entry_time = vehicle[key][1].split(" ")[1].split(":")
            exit_date = vehicle[key][2].split(" ")[0].split("-")
            exit_time = vehicle[key][2].split(" ")[1].split(":")
            b = datetime.datetime(int(entry_date[0]),int(entry_date[1]),int(entry_date[2]),int(entry_time[0]),int(entry_time[1]),int(entry_time[2].split(".")[0]))
            a = datetime.datetime(int(exit_date[0]),int(exit_date[1]),int(exit_date[2]),int(exit_time[0]),int(exit_time[1]),int(exit_time[2].split(".")[0]))
            diff = a-b
            x = diff.seconds/60
            print(f'difference  : {diff}')

      
