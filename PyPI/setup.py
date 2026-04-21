from pathlib import Path

from setuptools import find_packages, setup

BASE_DIR = Path(__file__).parent
README = (BASE_DIR / "README.md").read_text(encoding="utf-8")

setup(
    name="tiny-text-stats-2026",
    version="0.1.1",
    description="Small library for counting simple text statistics",
    long_description=README,
    long_description_content_type="text/markdown",
    author="FOSSDEV student",
    url="https://github.com/xx663xx/repo",
    project_urls={
        "Source": "https://github.com/xx663xx/repo",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={"tiny_text_stats": ["py.typed"]},
    include_package_data=True,
    python_requires=">=3.11",
    extras_require={
        "dev": [
            "build>=1.2.0",
            "mypy>=1.8.0",
            "pytest>=8.0.0",
            "ruff>=0.3.0",
            "setuptools>=68",
            "twine>=5.0.0",
            "wheel>=0.42.0",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
)
