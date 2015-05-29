import os
import sys
from setuptools import setup, find_packages

from pagarme.config import __version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read().strip()
requirements = ['requests', 'rsa']

setup(
    name='pagarmepy',
    version=__version__,
    description='Pagar.me Python API wrapper',
    long_description=readme,
    author='Michael Coelho',
    author_email='michael.tcoelho@gmail.com',
    url='https://github.com/michaeltcoelho/pagarme.py',
    download_url='https://github.com/michaeltcoelho/pagarme.py',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license='MIT License',
    test_suite='runtests',
    zip_safe=False,
    keywords='pagarme, payment, gateway, api, wrapper',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
