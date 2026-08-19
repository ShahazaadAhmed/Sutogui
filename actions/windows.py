from pywinauto import Desktop
from .base import Action


class TypeText(Action):

    def __init__(self, window_title, text):
        self.window_title = window_title
        self.text = text

    def execute(self):
        desktop = Desktop(backend="uia")

        window = desktop.window(
            title_re=f".*{self.window_title}.*"
        )

        window.wait("visible", timeout=10)

        document = window.child_window(
            control_type="Document"
        )

        document.wait("ready", timeout=10)
        document.set_focus()
        document.set_edit_text(self.text)

        return {
            "success": True,
            "message": f"Typed text into {self.window_title}"
        }