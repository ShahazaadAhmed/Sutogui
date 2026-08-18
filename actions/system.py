import time
from .base import Action


class Wait(Action):

    def __init__(self, seconds):
        self.seconds = seconds

    def execute(self):
        time.sleep(self.seconds)

        return {
            "success": True,
            "message": f"Waited {self.seconds} seconds"
        }