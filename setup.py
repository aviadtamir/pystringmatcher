import setuptools

with open("README.md") as _file:
    long_description = _file.read()

setuptools.setup(
    name="pystringmatcher",
    vcversioner={'vcs_args': ['git', 'describe', '--tags', '--long']},
    author="Aviad Tamir",
    author_email="aviadt15@gmail.com",
    description="A package for matching a set of strings and textual patterns in a given text file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aviadtamir/pystringmatcher.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires='>=3.7',
    install_requires=[
        "cached_property",
        "vcversioner"
    ],
    entry_points={
        'console_scripts': ['stringmatcher=pystringmatcher.__main__:main'],
    },
    license="MIT license",
    test_suite='tests',
    include_package_data=True,
)
