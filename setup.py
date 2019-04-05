import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fh:
    requirements = fh.read().split('\n')

setuptools.setup(
    name="LeanEuler",
    version="0.0.3",
    author="Sahil Gupta",
    author_email="",
    description="Lean implementation of core of EulerX functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/idaks/LeanEuler",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    scripts=['LeanEuler/CLI_Scripts/le_cleantax_to_asp',
             'LeanEuler/CLI_Scripts/le_cleantax_to_db',
             'LeanEuler/CLI_Scripts/le_db_to_asp',
             ]
)