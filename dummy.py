#!/usr/bin/env python3
from ev3dev.auto import *
import time

m = Motor(OUTPUT_A)
for i in range(10):
	m.run_timed(time_sp=3000, speed_sp=500)

