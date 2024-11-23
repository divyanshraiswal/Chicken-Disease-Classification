import setuptools

with open("README.md","r",encoding='utf-8') as f:
    long_decription=f.read()

__version__="0.0.0"

REPO_NAME="Chicken-Disease-Classification"
AUTHOR_USER_NAME="divyanshraiswal"
SRC_REPO="CHICKEN_DISEASE_CLASSIFICATION"
AUTHOR_EMAIL="divyansh.raiswal@gmail.com"
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_decription,
    long_description_content="text/markdown",
    url=f"XXXXXXXXXXXXXXXXXXX{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"XXXXXXXXXXXXXXXXXXX{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
