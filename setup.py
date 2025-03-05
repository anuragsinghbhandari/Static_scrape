from setuptools import setup

setup(
    name='StaticScrape',
    version='0.2',
    description = "A command line tool to clone any website's front end",
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
    }
)