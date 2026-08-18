import subprocess
from .base import Action


APPLICATIONS = {
    "chrome": "chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
}


class LaunchApplication(Action):

    def __init__(self, application):
        self.application = application.lower()

    def execute(self):
        executable = APPLICATIONS.get(self.application)

        if not executable:
            raise ValueError(
                f"Unknown application: {self.application}"
            )

        subprocess.Popen(executable)

        return {
            "success": True,
            "message": f"{self.application} launched"
        }