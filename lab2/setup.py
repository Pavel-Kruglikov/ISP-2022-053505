from setuptools import setup, find_packages

setup(
    name='serializer',
    version='1.0',
    author="Pavel Kruglikov",
    author_email="pavel.kruglikov.95@gmail.com",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'serializer = console_app:main',
        ],
    }
)