import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Site-Check",
    version="0.0.1",
    author="gege56015",
    author_email="gege56015@gege56015",
    description="A simple health checker for websites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gege56015/Site-Check",
    packages=setuptools.find_packages(),
    install_requires=['click', 'configparser', 'requests'],
    entry_points={
        'console_scripts': ['site-check=site_check.core:site_check']
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ),
)
