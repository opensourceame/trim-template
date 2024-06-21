from setuptools import setup

setup(
    name='trim-template',
    version='1.0',
    packages=['trim_template'],
    entry_points={
        'console_scripts': [
            'trim-template = trim_template.trim:main'
        ]
    }
)