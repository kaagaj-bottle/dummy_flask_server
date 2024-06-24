from setuptools import find_packages, setup

setup(
    name="flask_db",
    version="0.0.01",
    description="flask server with postgresql connection using psycopg2",
    author="Zishan Siddique",
    install_requires=[
        "pytest",
        "requests",
        "psycopg2-binary",
        "Flask",
        "Flask-Cors",
        "python-dotenv",
        "redis",
        "Flask-Session",
        "rq",
        "rq-scheduler",
    ],
    packages=find_packages(),
)
