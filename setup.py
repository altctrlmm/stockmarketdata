import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="altctrlmm", # Replace with your own username
    version="0.0.1",
    author="Micah",
    author_email="nothx@example.com",
    description="Robinhood Utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/rhutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
