from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='prodiapy',
version='2.4',
description='Prodia API Python Wrapper',
long_description=long_description,
long_description_content_type='text/markdown',
author='yoou3-cyber',
author_email='zenafey@eugw.ru',
packages=['prodia'],
license='MIT',
install_requires=['requests'])
