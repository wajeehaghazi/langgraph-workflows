from workflows.sequential_workflow import agent
from workflows.parallel_workflow import parallel_workflow
from workflows.router_workflow import router_workflow


def run_sequential():
    print("\nRunning Sequential Workflow\n")

    result = agent.invoke(
        {
            "topic": "cats"
        }
    )

    print(result)


def run_parallel():
    print("\nRunning Parallel Workflow\n")

    result = parallel_workflow.invoke(
        {
            "topic": "cats"
        }
    )

    print(result["combined_output"])


def run_router():
    print("\nRunning Router Workflow\n")

    result = router_workflow.invoke(
        {
            "input": "Write me a joke about cats"
        }
    )

    print(result["output"])


if __name__ == "__main__":

    print("\nSelect workflow to run:")
    print("1 - Sequential")
    print("2 - Parallel")
    print("3 - Router")

    choice = input("\nEnter choice: ")

    if choice == "1":
        run_sequential()

    elif choice == "2":
        run_parallel()

    elif choice == "3":
        run_router()

    else:
        print("Invalid choice")