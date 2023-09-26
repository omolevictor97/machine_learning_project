from setuptools import setup
from typing import List

def get_requirements() -> List[str]:

    """
    Description: This function returns a list of strings requirements
    in the requirements.txt file
    """
    
    with open("requirements.txt", "r") as files:
        requirements = [file.replace("\n", "") for file in files.readlines() if file != "-e ."]
        return requirements

setup(
    name="Housing Price Prediction",
    version="0.0.1",
    author="Victor Oshinonwu",
    author_email= "victoropeyemi97@outlook.com",
    long_description= "The program is intended to solve house price prediction",
    url="https://github.com/omolevictor97/machine_learning_project",
    packages=["housing"],
    license= "Apache License",
    install_requires = get_requirements()
)
