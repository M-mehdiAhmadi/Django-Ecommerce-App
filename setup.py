from setuptools import setup, find_packages

setup(
    name="",
    version="0.1.0",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    author="",
    author_email="",
    install_requires=[
        "Django>=5.0"
    ],
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
