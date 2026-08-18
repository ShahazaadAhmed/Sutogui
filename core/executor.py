class WorkflowExecutor:

    def execute(self, workflow):

        print(f"\nExecuting: {workflow.name}\n")

        for index, action in enumerate(workflow.actions, start=1):

            print(
                f"[{index}/{len(workflow.actions)}] "
                f"{action.__class__.__name__}"
            )

            try:
                result = action.execute()

                if result["success"]:
                    print(f"    ✓ {result['message']}")

            except Exception as error:

                print(f"    ✗ {error}")

                return False

        print("\nWorkflow completed successfully.")
        return True