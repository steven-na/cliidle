import curses

from loading_bar import make_progress_bar_string
from timed_loop import timed_loop_decorator


def setup():
    stdscr = curses.initscr()
    return stdscr


@timed_loop_decorator(tps=30, print_fps=False)
def main_loop(delta_time: float, screen: curses.window, data: dict):
    """Main tick loop"""
    screen.clear()

    fps = 1 / delta_time

    target_length = 15
    progress = (100*delta_time)/target_length

    screen.addstr(12, 10, f"{delta_time}")
    screen.addstr(10, 10, f"{fps:.02f}")
    screen.addstr(5, 5, make_progress_bar_string(data['progress'], 50, True))
    data['progress'] = data['progress'] + progress
    while data['progress'] >= 100.0:
        data['progress'] = data['progress'] - 100.0

    screen.refresh()


def simulation_main():
    stdscr = setup()
    main_loop(screen=stdscr, data={'progress': 0.0})
