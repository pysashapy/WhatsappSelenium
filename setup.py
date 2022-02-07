import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["requests<=2.21.0"]

setuptools.setup(
    name="hello_world_ericjaychi",
    version="0.0.1",
    author="Eric Chi",
    author_email="ericjaychi@gmail.com",
    description="A Hello World package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ericjaychi/sample-pypi-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
