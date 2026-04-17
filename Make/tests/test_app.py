from demo_app.calc import add, add_many
from demo_app.service import app, build_status_message


def test_add_uses_integer_arguments() -> None:
    assert add(2, 3) == 5


def test_add_many_sums_all_values() -> None:
    assert add_many([1, 2, 3]) == 6


def test_status_message_mentions_dependency() -> None:
    message = build_status_message("requests 2.x")
    assert "requests 2.x" in message


def test_fastapi_application_is_configured() -> None:
    assert app.title == "Make Demo Service"
