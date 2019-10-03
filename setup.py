import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-vishnuyar",
    version="0.0.4",
    author="vishnu yarmaneni",
    author_email="vardhanvishnu@gmail.com",
    description="Helper functions package for DataScience",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vishnuyar/lambdata-vishnuyar",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
