from core.workflow import Workflow
from core.executor import WorkflowExecutor

from actions.application import LaunchApplication
from actions.system import Wait
from actions.windows import Navigate


def main():

    workflow = Workflow(
        "Open Gmail"
    )

    workflow.add_action(
        LaunchApplication("chrome")
    )

    workflow.add_action(
        Wait(3)
    )

    workflow.add_action(
        Navigate(
            "Chrome",
            "https://mail.google.com"
        )
    )

    executor = WorkflowExecutor()

    executor.execute(workflow)


if __name__ == "__main__":
    main()