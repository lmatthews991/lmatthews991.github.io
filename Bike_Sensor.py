import RPi.GPIO as GPIO
import time
import csv

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

start = time.time()
wheel_c = 0
data =[]
distance = 0
rpm = 0.00
speed = 0.00
elapsed = 0.00


while True:
    input_state = GPIO.input(18)
    if input_state == False:
        timestamp = time.time()
        stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
        elapsed = time.time()
        distance += wheel_c
        rpm = 1/elapsed *60
        speed = (wheel_c*rpm*60)/1000
        print('Button Pressed', elapsed - start, distance, rpm, speed, timestamp, stamp)
        Start = elapsed
        time.sleep(0.2)
        data = [[rpm,speed,distance,elapsed,timestamp, stamp]]
        print(data)
        with open('testcsv.csv', 'a') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerows(data)
        f.close()
