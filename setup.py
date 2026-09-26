from pathlib import Path
from setuptools import setup


def get_requirements(filename: str = "requirements.txt") -> list[str]:
    """Reads dependencies from requirements.txt."""
    here = Path(__file__).parent.resolve()
    requirements_path = here / filename

    if not requirements_path.exists():
        return []

    with open(requirements_path, encoding="utf-8") as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith(("#", "-e", "--"))
        ]


setup(
    install_requires=get_requirements(),
    include_package_data=True,
)
