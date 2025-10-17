import argparse
import datetime as dt


def simulate_deployment(environment: str) -> None:
    """Print a timestamped message that simulates a deployment."""
    timestamp = dt.datetime.utcnow().isoformat()
    print(f"[{timestamp}] Deploying to {environment} environment")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simulate a deployment step.")
    parser.add_argument("environment", help="Environment name (e.g., test or prod)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    simulate_deployment(args.environment)


if __name__ == "__main__":
    main()
