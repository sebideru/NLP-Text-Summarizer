import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME="NLP-Text-Summarizer"
AUTHOR_USER_NAME="sebideru"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="seblewongelawash@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small  python package  for NLP Text Summarizer app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/"+AUTHOR_USER_NAME+"/"+SRC_REPO,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10'
)

