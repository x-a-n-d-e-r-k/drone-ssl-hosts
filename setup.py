from distutils.core import setup

setup(
    name='drone-ssl-hosts',
    version='1.0.0',
    author='XanderK',
    author_email='xanderk@notbo.red',
    scripts=['src/drone-ssl-hosts'],
    url='https://github.com/x-a-n-d-e-r-k/drone-ssl-hosts',
    license='LICENSE',
    description='Drone for importing hostnames based on SSL/TLS certificate information into Lair.',
    install_requires=[
        "pylair >= 2.0.0",
        "docopt >= 0.6.2",
        "ipaddr==2.1.11"
    ],
)
