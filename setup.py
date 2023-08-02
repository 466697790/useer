import sys

from setuptools import setup, find_packages

import useer

name = 'useer'
version = useer.__version__

# Validate Python version.
CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(
        f"""{name} requires Python {REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]}, 
        but you're trying to install it on Python {CURRENT_PYTHON[0]}.{CURRENT_PYTHON[1]}.""")
    sys.exit(1)

setup(
    name=name,
    version=version,
    description='A elaborate and developed PySpark libraries and resources.',
    author='liujinzhou',
    author_email='466697790@qq.com',
    url='https://github.com/466697790/useer',
    license=open('LICENSE', encoding='utf-8').read(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    # install_requires=open('requirements.txt').read().split('\n'),
    python_requires=f'>={REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]}',
    zip_safe=False,
    keywords=['apache', 'spark', 'sparkML', 'pmml'],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: Chinese (Simplified)',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    )
)
