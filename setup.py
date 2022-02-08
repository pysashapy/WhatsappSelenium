import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["requests<=2.21.0"]

setuptools.setup(
    name="pyWAppSel",
    version="1.0.4",
    author="Dark White",
    author_email="sasha.2000ibr@gmail.com",
    description="pyWAppSel is a selenium-based Whatsapp wrapper",
    long_description=long_description,
    install_requires=[
        'selenium',
        'webdriver_manager',
    ],
    long_description_content_type="text/markdown",
    url="https://github.com/pysashapy/pyWApp",
    packages=setuptools.find_packages(),
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
