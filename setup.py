import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='drone-ssl-hosts',
    version='1.0.0',
    author='XanderK',
    author_email='xanderk@notbo.red',
    scripts=['src/drone-ssl-hosts.py'],
    url='https://github.com/x-a-n-d-e-r-k/drone-ssl-hosts',
    license='LICENSE',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    long_description=long_description,
    description='Drone for importing hostnames based on SSL/TLS certificate information into Lair.',
    install_requires=[
        "pylair >= 2.0.0",
        "docopt >= 0.6.2",
        "ipaddr>=2.1.11"
    ],
)
