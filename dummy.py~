#!/usr/bin/env python3
from ev3dev.auto import *
import time

m = Motor(OUTPUT_A)
u=InfraredSensor(INPUT_4)

print("The maximun velocity is:",m.max_speed)
for i in range(10):
	m.run_timed(time_sp=3000, speed_sp=50*i)
	print ("The relative position is", m.position)
	print ("the velocity is", 50*i)
	print("The distances is", u.proximity)
	time.sleep(3)




