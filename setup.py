import setuptools
from pagarme.config import __version__


setuptools.setup(name='pagarme.py',
                 version=__version__,
                 description='Pagar.me Python API',
                 long_description=open('README.md').read().strip(),
                 author='Michael Coelho',
                 author_email='michael.tcoelho@gmail.com',
                 url='https://github.com/michaeltcoelho/pagarme.py',
                 py_modules=['pagarme'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='pagarme python rest api',
                 classifiers=['Packages'])
