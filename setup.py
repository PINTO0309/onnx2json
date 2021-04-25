from setuptools import setup, Extension
from setuptools import find_packages
from os import listdir

with open("README.md") as f:
    long_description = f.read()

scripts = ["scripts/"+i for i in listdir("scripts")]

if __name__ == "__main__":
    setup(
        name="onnx2json",
        scripts=scripts,
        version="1.0.0",
        description="Exports the ONNX file to a JSON file.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Katsuya Hyodo",
        author_email="rmsdh122@yahoo.co.jp",
        url="https://github.com/PINTO0309/onnx2json",
        license="MIT License",
        packages=find_packages(),
        platforms=["linux", "unix"],
        python_requires=">3.6",
    )
