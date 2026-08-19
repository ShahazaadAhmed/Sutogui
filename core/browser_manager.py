from pywinauto import Desktop
import time


class BrowserManager:

    def __init__(self):
        self.desktop = Desktop(backend="uia")

    def find_chrome(self):
        windows = self.desktop.windows()

        chrome_windows = []

        for window in windows:
            try:
                if window.class_name() == "Chrome_WidgetWin_1":
                    chrome_windows.append(window)
            except Exception:
                pass

        return chrome_windows

    def get_chrome_window(self, timeout=10):

        end_time = time.time() + timeout

        while time.time() < end_time:

            windows = self.find_chrome()

            if windows:
                # Prefer the first usable Chrome window.
                for window in windows:
                    try:
                        if window.is_visible():
                            return window
                    except Exception:
                        continue

            time.sleep(0.5)

        raise RuntimeError(
            "Could not find a Chrome window."
        )