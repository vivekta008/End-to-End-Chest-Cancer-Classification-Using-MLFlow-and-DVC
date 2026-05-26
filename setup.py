import setuptools




__version__ = "0.0.0"

REPO_NAME = "End-to-End-Chest-Cancer-Classification-Using-MLFlow-and-DVC"
AUTHOR_USER_NAME = "vivekta008"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "tavivek256@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)