from setuptools import find_packages, setup

__version__ = "0.0.0.1"

__doc__ = """Budker Institute Particle-in-Cell code (BIPIC)"""

packages = find_packages(".", include=["bipic"])

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bipic",
    version=__version__,
    author="Vyacheslav Fedorov",
    author_email="slava@fuodorov.ru",
    description=__doc__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/binp-dev/bipic",
    packages=packages,
    license="MIT",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
    ],
)
