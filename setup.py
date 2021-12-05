from setuptools import setup

setup(
    name="pxplore",
    version="0.1.0",
    packages=["pxplore"],
    nstall_requires=[
        'Click',
        'requests'
    ],
    entry_points={"console_scripts": ["pxplore = pxplore.__main__:main"]},
)

