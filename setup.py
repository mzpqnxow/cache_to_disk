import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cache_to_disk",
    version="2.0.0",
    author="Stewart Renehan",
    author_email="sarenehan@gmail.com",
    description="Local disk caching decorator for python function.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarenehan/cache_to_disk",
    packages=setuptools.find_packages(),
    requires_python=">3.4,<=3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
