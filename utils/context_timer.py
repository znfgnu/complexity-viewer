from time import perf_counter


class ContextTimer:
    def __enter__(self):
        self.finish_time = None
        self.start_time = perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.finish_time = perf_counter()

    def get_elapsed(self) -> float:
        if self.finish_time is None: return None
        return self.finish_time - self.start_time
