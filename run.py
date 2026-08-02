import subprocess
import time

from app.cli.main import main


def start_docker() -> None:

    print("Starting Docker services...")

    subprocess.run(
        ["docker", "compose", "up", "-d"],
        check=True,
    )

    print("Waiting for services...")

    time.sleep(5)


def run() -> None:

    start_docker()

    print("\nOpen the browser to upload documents:")
    print("http://localhost:8000/docs\n")

    main()


if __name__ == "__main__":
    run()