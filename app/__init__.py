"""Application package marker and version helper."""

from importlib import metadata


def get_version() -> str:
    """Return the installed package version, or a default during local usage."""
    try:
        return metadata.version("githubactions")
    except metadata.PackageNotFoundError:
        return "0.0.0"


__all__ = ["get_version"]
