from setuptools import setup

setup(
    name='StaticScrape',
    version='0.1',
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