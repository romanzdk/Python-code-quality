from setuptools import find_packages, setup

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=["flask==2.0.1", "requests==2.25.1"],
    extras_require={"dev": ["pytest", "flake8", "black", "mypy"]},
    entry_points={
        "console_scripts": [
            "my_package=my_package.main:main",
        ],
    },
)
