from utils.timed_loop import timed_loop_decorator


def setup():
    pass


@timed_loop_decorator(tps=60, print_fps=False)
def main_loop(delta_time: float, data: dict):
    """Main tick loop"""
    # START OF LOOP

    data['fps'] = 1 / delta_time

    target_length = 25
    progress = (100*delta_time)/target_length

    data['progress'] = data['progress'] + progress
    while data['progress'] >= 100.0:
        data['progress'] = data['progress'] - 100.0
        data['loopcount'] = data['loopcount'] + 1

    # END OF LOOP


def simulation_main(data: dict):
    main_loop(data=data)
