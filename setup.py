from setuptools import setup, find_packages

setup(
    name="agent-x",
    version="1.0.0",
    author="Haragam Deep",
    author_email="haragam.22@gmail.com",
    description="An AI-powered tool for automated webpage maintenance using LLMs",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/haragam22/agent-x",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi",
        "uvicorn",
        "beautifulsoup4",
        "selenium",
        "openai",
        "langchain",
        "requests",
        "python-dotenv",
        "pydantic",
        "lighthouse-py",
        "pytest"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "agentx=src.app.main:app",
        ],
    },
)
