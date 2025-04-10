from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="perplexityai",
    version="0.1",
    description="A python api to use perplexity.ai",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nathanrchn/perplexityai",
    packages=find_packages(),
    install_requires=["websocket-client>=1.2.0", "requests>=2.20.0"]
)
