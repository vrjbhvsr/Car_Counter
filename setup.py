from setuptools import setup, find_packages

with open('README.md','r', encoding="utf-8") as f:
    descriptions = f.read()


setup(
    name= "Car Counter",
    version= "0.0.1",
    author= "Vraj Bhavsar",
    author_email= "vrajcbhavsar0905@gmail.com",
    description= "small python package for Car Counting app.",
    long_description= descriptions,
    long_description_content = "text/markdown",
    url = "https://github.com/vrjbhvsr/Car_Counter",
    package_dir= {"":"Car_Counter"},
    packages= find_packages(where="Car_Counter")
)