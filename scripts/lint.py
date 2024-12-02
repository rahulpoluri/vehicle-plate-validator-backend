import subprocess


def run_tool(tool: str, *args) -> None:
    print(f"Running {tool} with params {list(args)}")
    try:
        result = subprocess.run([tool, *args], capture_output=True)

    except Exception as e:
        print(e)
    if result.returncode != 0:
        print(result.returncode)
        print(result.stderr.decode())
        print(result.stdout.decode())
    else:
        print(result.stderr.decode())
        print(result.stdout.decode())
        print(f"{tool} ran completed successfully, without errors")
    print("*" * 50)


def main() -> None:
    run_tool("black", ".")
    run_tool("flake8", ".")
    run_tool("isort", ".")
    run_tool("mypy", ".")
