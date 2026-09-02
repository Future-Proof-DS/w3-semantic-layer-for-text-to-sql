"""Load project secrets from a local .env file."""

from dotenv import load_dotenv

from agent.paths import PROJECT_ROOT


def load_project_env() -> None:
    """Load variables from .env at the project root if present."""
    load_dotenv(PROJECT_ROOT / ".env")
