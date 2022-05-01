from setuptools import setup

setup(
    name='app-example',
    version='0.0.1',
    author='Ivan K',
    author_email='ivankurban1986@gmail.com',
    description='FastApi app',
    install_requires=[
        'fastapi==0.75.2',
        'uvicorn==0.17.6',
        'SQLAlchemy==1.4.26',
        'pytest==7.1.2',
        'requests==2.27.1',
    ],
    scripts=['app/main.py', 'scripts/create_db.py']
)