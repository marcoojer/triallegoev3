#!/usr/bin/env python3
from ev3dev.ev3 import *
import time

m = LargeMotor(OUTPUT_A)
u=InfraredSensor(INPUT_4)

print("The maximun velocity is:",m.max_speed)
for i in range(10):
	if i%2==0:
		m.run_to_rel_pos(position_sp=1080,speed_sp=500)
	else:
		m.run_to_rel_pos(position_sp=-1080,speed_sp=500)
	
	m.wait_while('running')
	print("Motor position",m.position)




