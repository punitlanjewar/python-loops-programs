# Double the wait time while next attempt

import time

wait_time = 1
max_reattempts = 5
attempts = 0

while attempts < max_reattempts:
    print('Attempt', attempts + 1, '-wait time', wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1