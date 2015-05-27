import setuptools
from pagarme.config import __version__


setuptools.setup(name='pagarme.py',
                 version=__version__,
                 description='Pagar.me`s Python API',
                 long_description=open('README.md').read().strip(),
                 author='Curiosity',
                 author_email='michael.tcoelho@gmail.com',
                 url='https://github.com/michaeltcoelho/pagarme.py',
                 py_modules=['pagar.me', 'pagarme.py'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='pagarme python rest api',
                 classifiers=['Packages'])
