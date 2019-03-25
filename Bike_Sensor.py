import RPi.GPIO as GPIO
import time
import csv
import datetime

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
t = time.time()
t2 = time.time()
distance = 0
wheel_c = 20

with open('testcsv.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "elapsed", "rpm", "speed", "distance", "duration"])
f.close()

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        timestamp = time.time()
        stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
        newt = time.time()
        elapsed = newt - t
        duration = time.time() - t2
        distance += wheel_c
        rpm = 1/elapsed *60
        speed = (wheel_c*rpm*60)/1000
        print('Sensor Triggered', elapsed, distance, duration, rpm, speed, timestamp, stamp)
        t = newt
        time.sleep(0.2)
        
        
        # Store Data in List
        data = [[stamp, elapsed, rpm, speed, distance, duration]]
        print(data)
        
        #Append to csv 
        with open('testcsv.csv', 'a') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerows(data)
        f.close()
        
        # Reinitialise Start
        
        time.sleep(0.2)   
       
