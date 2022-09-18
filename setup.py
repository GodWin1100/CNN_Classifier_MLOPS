import setuptools

with open("./README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "CNN_Classifier_MLOPS"
SRC_REPO = "deepclassifier"
AUTHOR_USER_NAME = "GodWin1100"
AUTHOR_EMAIL = "shivamjpanchal1@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Deep CNN Classifier with MLOPS",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
