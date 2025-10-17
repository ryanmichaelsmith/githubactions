from app import get_version
from app.main import hello


def test_hello_returns_expected_greeting():
    assert hello() == "Hello, World!"


def test_get_version_defaults_when_package_missing():
    assert get_version() == "0.0.0"
