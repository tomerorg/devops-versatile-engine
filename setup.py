
from setuptools import setup, find_packages

setup(
    name="devops-versatile-engine",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pandas>=1.2.0",
        "numpy>=1.20.0",
    ],
    author="",
    author_email="",
    description="Experimental devops project using Celery and SQLAlchemy in Python",
    keywords="devops-versatile-engine, python",
    url="",
)
