import argparse
import datetime as dt
from typing import Optional


def simulate_deployment(environment: str, version: Optional[str]) -> None:
    """Print a timestamped message that simulates a deployment."""
    timestamp = dt.datetime.utcnow().isoformat()
    version_fragment = f" version {version}" if version else ""
    print(f"[{timestamp}] Deploying{version_fragment} to {environment} environment")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simulate a deployment step.")
    parser.add_argument("environment", help="Environment name (e.g., test or prod)")
    parser.add_argument(
        "--version",
        help="Optional version string to report alongside the deployment",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    simulate_deployment(args.environment, args.version)


if __name__ == "__main__":
    main()
