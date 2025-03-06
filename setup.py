from setuptools import setup

# Read the README file for PyPI description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='StaticScrape',
    version='0.2.1',
    description="A command-line tool to clone any website's front end",
    long_description=long_description,  # This ensures the README appears on PyPI
    long_description_content_type="text/markdown",  # Specify markdown format
    author='Anurag Singh Bhandari',
    author_email='anuoo3ups@gmail.com',
    packages=['StaticScrape'],
    install_requires=[
        'playwright',
        'beautifulsoup4',
        'lxml'
    ],
    entry_points={
        'console_scripts': [
            'staticscrape = StaticScrape.front_clone:main'
        ]
    },
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,  # Ensures LICENSE & README.md are included
    python_requires='>=3.6',
)
