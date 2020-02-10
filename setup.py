import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ally_rh_csv",
    version="0.0.1",
    author="altctrlmm",
    author_email="micahmrocks@gmail.com",
    description="Download Ally and Robinhood download to CSV.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/altctrlmm/ally_rh_csv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["ally", "robinhood", "CSV", "stock quotes",
              "finance", "stocks", "options", "trading", "investing"],
    python_requires='>=3.5',
)
