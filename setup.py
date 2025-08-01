from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="my_simple_math",
    version="0.1.0",
    packages=find_packages(),
    description="A simple math library for learning package distribution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="STANSLOUS MUSAYA",
    author_email="musayalous@gmail.com",
    url="https://github.com/MSTANSLOUS/my_simple_math",  # Removed .git from the end
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    test_suite="tests",
)