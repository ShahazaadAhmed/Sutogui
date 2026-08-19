from .base import Action
from core.window_manager import WindowManager
from core.browser_manager import BrowserManager

class TypeText(Action):

    def __init__(self, window_title, text):
        self.window_title = window_title
        self.text = text

    def execute(self, context):

        manager = WindowManager()

        window = manager.wait_for_window(
            title_re=f".*{self.window_title}.*"
        )

        document = manager.wait_for_control(
            window,
            control_type="Document"
        )

        document.set_focus()

        document.type_keys(
            self.text,
            with_spaces=True,
            pause=0.05
        )

        return {
            "success": True,
            "message": (
                f"Typed text into "
                f"{self.window_title}"
            )
        }
class Click(Action):

    def __init__(
        self,
        window_title,
        control_type=None,
        control_title=None
    ):
        self.window_title = window_title
        self.control_type = control_type
        self.control_title = control_title

    def execute(self, context):

        manager = WindowManager()

        window = manager.wait_for_window(
            title_re=f".*{self.window_title}.*"
        )

        control = manager.wait_for_control(
            window,
            control_type=self.control_type,
            title=self.control_title
        )

        control.click_input()

        return {
            "success": True,
            "message": (
                f"Clicked "
                f"{self.control_title or self.control_type}"
            )
        }
class PressKey(Action):

    def __init__(self, window_title, key):
        self.window_title = window_title
        self.key = key

    def execute(self, context):

        manager = WindowManager()

        window = manager.wait_for_window(
            title_re=f".*{self.window_title}.*"
        )

        window.set_focus()
        window.type_keys(self.key)

        return {
            "success": True,
            "message": f"Pressed {self.key}"
        }
class WaitForWindow(Action):

    def __init__(
        self,
        window_title,
        timeout=10
    ):
        self.window_title = window_title
        self.timeout = timeout

    def execute(self, context):

        manager = WindowManager()

        manager.wait_for_window(
            title_re=f".*{self.window_title}.*",
            timeout=self.timeout
        )

        return {
            "success": True,
            "message": (
                f"Window '{self.window_title}' "
                f"is ready"
            )
        }
class Navigate(Action):

    def __init__(self, application, url):
        self.application = application.lower()
        self.url = url

    def execute(self, context):

        if self.application != "chrome":
            raise ValueError(
                "Navigate currently supports Chrome only."
            )

        browser = BrowserManager()

        window = browser.get_chrome_window()

        context.set(
            "active_window",
            window
        )

        window.set_focus()

        window.type_keys(
            "^l",
            pause=0.05
        )

        window.type_keys(
            self.url,
            with_spaces=True,
            pause=0.03
        )

        window.type_keys(
            "{ENTER}",
            pause=0.05
        )

        return {
            "success": True,
            "message": (
                f"Navigated to {self.url}"
            )
        }