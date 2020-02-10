import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ally_rh_csv",
    version="0.2.3",
    author="altctrlmm",
    author_email="micahmrocks@gmail.com",
    description="Robinhood and Ally download to CSV.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/altctrlmm/ally_rh_csv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["alphavantage", "historical quotes", "robinhood", "stocks",
              "finance", "options", "trading", "investing"],
    python_requires='>=3.5',
)
