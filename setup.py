import sys
from setuptools import setup

setup(
    name="fasticule",
    version="0.0.1",
    install_requires=[
        "fastapi ~= 0.86.0",
        "uvicorn[standard] ~= 0.19.0",
    ],
    extras_require={
        "dev": [
            "black ~= 22.10.0",
            "pytest ~= 7.1.3",
            "requests==2.28.1",
        ]
    },
    python_requires=">=3.9",
)
