import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ccorp-yaml-include",
    version="0.0.2",
    author="Tristan Sweeney",
    author_email="tristan.sweeney@cambridgeconsultants.com",
    description="An extension of ruamel.yaml to support including aliases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/pypa/sampleproject",
    packages=['ccorp.ruamel.yaml.include'],
    install_requires = ['ruamel.yaml'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
