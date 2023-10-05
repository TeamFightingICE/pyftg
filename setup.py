from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyftg",
    version="1.1",
    author="Staciiaz",
    description="An interface for implementing python AI in DareFightingICE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TeamFightingICE/pyftg",
    python_requires=">=3.10",
    install_requires=["grpcio", "grpcio-tools", "protobuf", "numpy"],
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    include_package_data=True,
)
