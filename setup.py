from setuptools import setup, find_packages

setup(
    name="pyftg",
    version="1.0",
    author="TeamDareFightingICE",
    description="An interface for implementing python AI in DareFightingICE",
    python_requires=">=3.8",
    install_requires=["grpcio"],
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    include_package_data=True,
)
