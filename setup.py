import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stockmarketdata",
    version="0.0.1",
    author="altctrlmm",
    author_email="micahmrocks@gmail.com",
    description="Download current and historical stock quotes to CSV files. Built on the Ally, Robinhood, and AlphaVantage APIs and relies on their free keys.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/altctrlmm/stockmarketdata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["ally", "robinhood", "CSV", "stock quotes",
              "finance", "stocks", "options", "trading", "investing", "AlphaVantage"],
    python_requires='>=3.5',
)
