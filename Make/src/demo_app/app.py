import requests

from demo_app.service import build_status_message


def main() -> None:
    print("Running app")
    print(build_status_message(f"requests {requests.__version__}"))


if __name__ == "__main__":
    main()
