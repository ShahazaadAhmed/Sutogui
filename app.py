from core.workflow import Workflow
from core.executor import WorkflowExecutor

from actions.application import LaunchApplication
from actions.browser import OpenURL
from actions.system import Wait


def main():

    workflow = Workflow("Open Gmail")

    workflow.add_action(
        LaunchApplication("chrome")
    )

    workflow.add_action(
        Wait(2)
    )

    workflow.add_action(
        OpenURL("https://mail.google.com")
    )

    executor = WorkflowExecutor()

    executor.execute(workflow)


if __name__ == "__main__":
    main()