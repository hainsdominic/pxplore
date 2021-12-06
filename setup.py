from setuptools import setup

setup(
    name="pxplore",
    version="0.1.0",
    packages=["pxplore"],
    install_requires=[
        'click',
        'requests',
        'pandas'
    ],
    entry_points={"console_scripts": ["pxplore = pxplore.__main__:main"]},
)

