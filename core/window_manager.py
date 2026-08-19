from pywinauto import Desktop


class WindowManager:

    def __init__(self, backend="uia"):
        self.desktop = Desktop(backend=backend)

    def get_window_handles(self):
        return {
            window.handle
            for window in self.desktop.windows()
        }

    def find_new_window(
        self,
        previous_handles,
        title_re=None,
        timeout=15
    ):
        import time

        end_time = time.time() + timeout

        while time.time() < end_time:

            windows = self.desktop.windows()

            for window in windows:

                try:
                    if window.handle in previous_handles:
                        continue

                    if title_re:
                        title = window.window_text()

                        if not __import__(
                            "re"
                        ).match(title_re, title):
                            continue

                    window.wait(
                        "visible",
                        timeout=2
                    )

                    return window

                except Exception:
                    continue

            time.sleep(0.5)

        raise RuntimeError(
            "No new window appeared within "
            f"{timeout} seconds."
        )