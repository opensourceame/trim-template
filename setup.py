from setuptools import setup

setup(
    name='trim-template',
    version='1.0',
    packages=['trim'],
    entry_points={
        'console_scripts': [
            'trim = trim-template.trim:main'
        ]
    }
)