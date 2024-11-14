import time


def timed_loop_decorator(tps: int, print_fps: bool = True):
    def wrap(f):
        def main_loop(*args, **kwargs):
            target_frame_time = 1 / tps
            last_time = time.perf_counter()
            delta_time = time.perf_counter()
            while True:
                fps = 1/delta_time
                if print_fps is True:
                    print(f"FPS: {fps}")
                current_time = time.perf_counter()
                delta_time = current_time - last_time
                last_time = current_time
                r = f(delta_time, *args, **kwargs)
                sleep_time = target_frame_time - \
                    (time.perf_counter() - current_time)
                time.sleep(max(0, sleep_time))
            return r
        return main_loop
    return wrap
