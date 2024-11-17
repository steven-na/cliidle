"""Main file"""

import time
from threading import Thread

from display.main import display_main
from simulation.main import simulation_main

if __name__ == "__main__":
    data = {'progress': 0.0, 'loopcount': 0, 'test_val': 0, 'fps': 0}
    disp_thread = Thread(target=display_main, args=(data,), daemon=True)
    disp_thread.start()

    sim_thread = Thread(target=simulation_main, args=(data,), daemon=True)
    sim_thread.start()
    while (True):
        print(data)
        data['test_val'] = data['test_val'] + 1
        time.sleep(.05)
