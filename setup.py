from setuptools import setup, find_packages

VERSION = '0.0.0.1'
DESCRIPTION = 'Budgeting App'
LONG_DESCRIPTION = 'An app that helps with budgeting'

# Setting up
setup(
    name="expense ",
    version=VERSION,
    author="Human Ai",
    author_email="<tarini.m.ap@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)