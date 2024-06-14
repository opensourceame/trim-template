from setuptools import setup

setup(
    name='skimpy',
    version='1.0',
    packages=['skimpy'],
    entry_points={
        'console_scripts': [
            'skimpy = skimpy.skimpy:main'
        ]
    }
)