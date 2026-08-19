import os
import subprocess
from .base import Action
from core.window_manager import WindowManager


APPLICATION_PATHS = {
    "chrome": [
        os.path.expandvars(
            r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"
        ),
        os.path.expandvars(
            r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
        ),
        os.path.expandvars(
            r"%LocalAppData%\Google\Chrome\Application\chrome.exe"
        ),
    ],
    "notepad": [
        r"C:\Windows\System32\notepad.exe"
    ],
    "calculator": [
        r"C:\Windows\System32\calc.exe"
    ],
}


def find_executable(application):
    paths = APPLICATION_PATHS.get(application.lower())

    if not paths:
        raise ValueError(
            f"Unsupported application: {application}"
        )

    for path in paths:
        if path and os.path.isfile(path):
            return path

    raise FileNotFoundError(
        f"Could not find {application}."
    )


class LaunchApplication(Action):

    def __init__(self, application):
        self.application = application.lower()
        self.process = None

    def execute(self, context):

        executable = find_executable(self.application)
        process = subprocess.Popen([executable])
        context.set("active_pid", process.pid)
        context.set("active_application", self.application)
        return {
            "success": True,
            "message": (
                f"{self.application} launched "
                f"(PID: {process.pid})"
            )
        }