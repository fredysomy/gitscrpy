from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Fredy Somy",
    author_email="fredysomy@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="A python library to scrape github",
    install_requires=['beautifulsoup4','html5lib','requests'],
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    
    version="0.3.2",
    keywords="gitscrpy",
    name="gitscrpy",
    packages=find_packages(),
    
    setup_requires=[],
    url="https://github.com/fredysomy/git_scraper",
  
    zip_safe=False,
)
