from .base import Action
from core.window_manager import WindowManager


class TypeText(Action):

    def __init__(self, window_title, text):
        self.window_title = window_title
        self.text = text

    def execute(self):

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

    def execute(self):

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