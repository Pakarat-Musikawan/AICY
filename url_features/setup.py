from setuptools import setup, find_packages

setup(
    name="url_features",
    packages=find_packages(),
    install_requires=[
        'tldextract',
    ],
)
