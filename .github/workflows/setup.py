from setuptools import setup, find_packages

setup(
    name="smart-testing-showcase",
    version="0.1.0",
    description="A showcase project for smart testing in Python",
    author="Ken Dallmier",
    packages=find_packages(where="src/main"),
    package_dir={"": "src/main"},
    install_requires=[
        # List your packages, e.g. 'requests', 'flask'
    ],
    python_requires=">=3.11",
)
