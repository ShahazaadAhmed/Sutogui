import webbrowser
from .base import Action


class OpenURL(Action):

    def __init__(self, url):
        self.url = url

    def execute(self):
        webbrowser.open(self.url)

        return {
            "success": True,
            "message": f"Opened {self.url}"
        }