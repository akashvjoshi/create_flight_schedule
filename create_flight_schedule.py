source_airport = ['AUS', 'DAL' , 'HOU']
destination_airport = ['AUS', 'DAL' , 'HOU']
tails = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']
flight_times = {'AUSDAL' : 50, 'AUSHOU' : 45, 'DALHOU' : 65, 'DALAUS' : 50, 'HOUAUS' : 45, 'HOUDAL' : 65}
gates = {'AUS' : 1, 'DAL' : 2, 'HOU' : 3}
ground_time = {'AUS' : 25, 'DAL' : 30, 'HOU' : 35}
flights = []
start_time = 360
end_time = 1320

def militarytimes(mins):
    if mins < 720:
        hour = mins // 60 
        minute = mins % 60
        return("{0:02d}{1:02d}".format(hour, minute))
    elif mins == 720:
        hour = 1200
        return("1200")
    else:
        hour = ((mins-720) // 60) + 12
        minute = (mins) % 60
        return("{0:02d}{1:02d}".format(hour, minute))

#for T1 from Austin to Houston
start_time = 360
departure_A_T1 = start_time

while start_time < end_time:
    arrival_H_T1 = departure_A_T1 + flight_times['AUSHOU']
    flights.append([tails[0], source_airport[0] , destination_airport[2] , militarytimes(departure_A_T1), militarytimes(arrival_H_T1)])
    departure_H_T1 = arrival_H_T1 + ground_time['HOU']
    arrival_A_T1 = departure_H_T1 + flight_times['HOUAUS']
    if (arrival_A_T1 + ground_time['AUS'] )  > end_time:
        break
    flights.append([tails[0], source_airport[2] , destination_airport[0] , militarytimes(departure_H_T1), militarytimes(arrival_A_T1)])
    departure_A_T1 = arrival_A_T1 + ground_time['AUS']
    
    start_time = departure_A_T1
    
final_schedule = '\n'.join(map(str,flights))

#for T2 from Dallas to Huouston
start_time = 360
departure_D_T2 = start_time

while start_time < end_time:
    arrival_H_T2 = departure_D_T2 + flight_times['DALHOU']
    flights.append([tails[1], source_airport[1] , destination_airport[2] , militarytimes(departure_D_T2), militarytimes(arrival_H_T2)])
    departure_H_T2 = arrival_H_T2 + ground_time['HOU']
    arrival_D_T2 = departure_H_T2 + flight_times['HOUDAL']
    flights.append([tails[1], source_airport[2] , destination_airport[1] , militarytimes(departure_H_T2), militarytimes(arrival_D_T2)])
    departure_D_T2 = arrival_D_T2 + ground_time['DAL']
    start_time = departure_D_T2
final_schedule = '\n'.join(map(str,flights))

#for T3 from Dallas to Houston
start_time = 360
departure_D_T3 = start_time

while start_time < end_time:
    arrival_H_T3 = departure_D_T3 + flight_times['DALHOU']
    flights.append([tails[2], source_airport[1] , destination_airport[2] , militarytimes(departure_D_T3), militarytimes(arrival_H_T3)])
    departure_H_T3 = arrival_H_T3 + ground_time['HOU']
    arrival_D_T3 = departure_H_T3 + flight_times['HOUDAL']
    flights.append([tails[2], source_airport[2] , destination_airport[1] , militarytimes(departure_H_T3), militarytimes(arrival_D_T3)])
    departure_D_T3 = arrival_D_T3 + ground_time['DAL']
    start_time = departure_D_T3
final_schedule = '\n'.join(map(str,flights))

#for T4 from Houston to Austin
start_time = 360
departure_H_T4 = (start_time + 5)

while start_time < end_time:
    arrival_A_T4 = departure_H_T4 + flight_times['HOUAUS']
    flights.append([tails[3], source_airport[2] , destination_airport[0] , militarytimes(departure_H_T4), militarytimes(arrival_A_T4)])
    departure_A_T4 = arrival_A_T4 + ground_time['AUS']
    arrival_H_T4 = departure_A_T4 + flight_times['AUSHOU']
    if (arrival_H_T4 + ground_time['HOU'] )  > end_time:
        break
    flights.append([tails[3], source_airport[0] , destination_airport[2] , militarytimes(departure_A_T4), militarytimes(arrival_H_T4)])
    departure_H_T4 = arrival_H_T4 + ground_time['HOU']
    start_time = departure_H_T4
final_schedule = '\n'.join(map(str,flights))

#for T5 from Houston to Dallas
start_time = 360
departure_H_T5 = start_time

while start_time < end_time:
    arrival_D_T5 = departure_H_T5 + flight_times['HOUDAL']
    flights.append([tails[4], source_airport[2] , destination_airport[1] , militarytimes(departure_H_T5), militarytimes(arrival_D_T5)])
    departure_D_T5 = arrival_D_T5 + ground_time['DAL']
    arrival_H_T5 = departure_D_T5 + flight_times['DALHOU']
    flights.append([tails[4], source_airport[1] , destination_airport[2] , militarytimes(departure_D_T5), militarytimes(arrival_H_T5)])
    departure_H_T5 = arrival_H_T5 + ground_time['HOU']
    start_time = departure_H_T5
final_schedule = '\n'.join(map(str,flights))

#for T6 from Houston to Dallas
start_time = 360
departure_H_T6 = start_time

while start_time < end_time:
    arrival_D_T6 = departure_H_T6 + flight_times['HOUDAL']
    flights.append([tails[5], source_airport[2] , destination_airport[1] , militarytimes(departure_H_T6), militarytimes(arrival_D_T6)])
    departure_D_T6 = arrival_D_T6 + ground_time['DAL']
    arrival_H_T6 = departure_D_T6 + flight_times['DALHOU']
    flights.append([tails[5], source_airport[1] , destination_airport[2] , militarytimes(departure_D_T6), militarytimes(arrival_H_T6)])
    departure_H_T6 = arrival_H_T6 + ground_time['HOU']
    start_time = departure_H_T6
final_schedule = '\n'.join(map(str,flights))
#print(flights)
print(final_schedule)

#sort the flight schedule according to tail number and departure time
#flight_schedule_sorted = '\n'.join(map(str,sorted(flights, key = lambda x: x[0] + x[3])))
#print(flight_schedule_sorted)

import csv
csv_header = 'tail_number,origin,destination,departure_time,arrival_time'
csvfile = "E:/Study Material/Fall 17/Programming for data science/Programming Labs/flight_schedule.csv"
with open(csvfile, "w") as output:
    print(csv_header, file = output)
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(flights)