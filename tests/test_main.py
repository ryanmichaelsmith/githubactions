from app.main import hello


def test_hello_returns_expected_greeting():
    assert hello() == "Hello, World!"
