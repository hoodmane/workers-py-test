"""Workers Runtime SDK - Dummy package for CI/CD testing."""

__version__ = "1.0.0"


class Request:
    """Dummy Request class."""

    def __init__(self, url: str, method: str = "GET") -> None:
        self.url = url
        self.method = method


class Response:
    """Dummy Response class."""

    def __init__(self, body: str, status: int = 200) -> None:
        self.body = body
        self.status = status


def handler(func):  # type: ignore[no-untyped-def]
    """Dummy handler decorator."""

    def wrapper(*args, **kwargs):  # type: ignore[no-untyped-def]
        return func(*args, **kwargs)

    return wrapper


__all__ = ["Request", "Response", "handler", "__version__"]
