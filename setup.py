from setuptools import setup, find_packages

from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read() 

HYPHEN_E_DOT = "-e ."  

def get_requirements(filepath: str) -> List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

__version__ = "0.0.1"
REPO_NAME = "KeyTitan"
PKG_NAME= "keytitan"
AUTHOR_USER_NAME = "suryanshp1"
AUTHOR_EMAIL = "suryanshp1@gmailcom"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for generating strong password.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("requirements.txt"),
)