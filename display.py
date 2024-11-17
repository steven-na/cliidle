import curses

from loading_bar import make_progress_bar_string
from timed_loop import timed_loop_decorator


def setup():
    stdscr = curses.initscr()
    return stdscr


@timed_loop_decorator(tps=20, print_fps=False)
def main_loop(delta_time: float, screen: curses.window, data: dict):
    """Main tick loop"""
    screen.clear()
    # START OF LOOP

    screen.addstr(12, 10, f"{delta_time}")
    screen.addstr(8, 10, f"{data['loopcount']} loops")
    screen.addstr(13, 10, f"{data['test_val']}")
    screen.addstr(10, 10, f"Sim fps: {data['fps']:.02f}")
    screen.addstr(5, 5, make_progress_bar_string(data['progress'], 50, True))

    # END OF LOOP
    screen.refresh()


def display_main(data: dict):
    stdscr = setup()
    main_loop(screen=stdscr, data=data)
