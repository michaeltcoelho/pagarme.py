import setuptools
from pagarme.config import __version__


setuptools.setup(name='pygarme',
                 version=__version__,
                 description='Pagar.me`s Python API',
                 long_description=open('README.md').read().strip(),
                 author='Curiosity',
                 author_email='michael.tcoelho@gmail.com',
                 url='http://path-to-my-packagename',
                 py_modules=['pygarme'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='pagarme python api',
                 classifiers=['Packages'])
