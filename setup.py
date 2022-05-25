from setuptools import setup
# NOTE: necessary to import __version__
# exec(open("apple_heartrate_pandas/_version.py").read())

from os import path
with open(path.join(path.abspath(path.dirname(__file__)), "README.md")) as f:
    readme = f.read()

setup(
    name='execution_time_wrapper',
    version="1.0.0",
    license='MIT',
    url='https://github.com/LeonardoAlchieri/ExecutionTimeWrapper',
    author='Leonardo Alchieri',
    author_email='leonardo@alchieri.eu',
    description='A Python package with some simple wrapper functions to print the execution time of methods',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords=['time', 'wrapper', 'log', 'print', 'execution', 'speed'],
    packages=['execution_time_wrapper'],
    # py_modules=['apple_heartrate_pandas'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
    install_requires=[
    'python_version>="3.6"',
]
)