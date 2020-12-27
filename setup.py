import setuptools

with open("README.md") as _file:
    long_description = _file.read()

setuptools.setup(
    name="pystringmatcher",
    version="0.0.0",
    author="Aviad Tamir",
    author_email="aviadt15@gmail.com",
    description="A package for matching a set of strings and textual patterns in a given text file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.7',
    install_requires=[
        "cached_property"
    ],
    entry_points={
        'console_scripts': ['stringmatcher=pystringmatcher.__main__:main'],
    }
)
