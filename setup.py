# setup.py

from setuptools import setup, find_packages

setup(
    name="enbdleap-python-core",
    version="0.1.0",
    description="A FastAPI Dependency Injection framework with support for scoped dependencies and middleware",
    author="Mohammed Ashfaq",
    author_email="MohammedPA@emiratsnbd.com",
    url="",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "pydantic>=1.8.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    include_package_data=True,
    long_description_content_type='text/markdown',
    license='MIT',
)
