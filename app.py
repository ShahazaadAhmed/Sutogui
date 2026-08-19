from core.workflow import Workflow
from core.executor import WorkflowExecutor

from actions.application import LaunchApplication
from actions.system import Wait
from actions.windows import TypeText, Click


def main():

    workflow = Workflow("Test Windows Automation")

    workflow.add_action(
        LaunchApplication("notepad")
    )

    workflow.add_action(
        Wait(2)
    )

    workflow.add_action(
        TypeText(
            "Notepad",
            "TaskFlow click test"
        )
    )

    workflow.add_action(
        Click(
            window_title="Notepad",
            control_type="MenuItem",
            control_title="File"
        )
    )

    executor = WorkflowExecutor()

    executor.execute(workflow)


if __name__ == "__main__":
    main()