from fastapi import FastAPI

app = FastAPI(title="Make Demo Service")


def build_status_message(dependency_name: str) -> str:
    return f"Project environment is active: {dependency_name} is available."
