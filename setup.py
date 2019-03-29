from setuptools import setup
from os import path

# Get the long description from the README file
with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='loss_landscapes',
    version='0.1.0',
    packages=['loss_landscapes'],
    url='https://github.com/marcellodebernardi/loss-landscapes',
    license='MIT',
    author='Marcello De Bernardi',
    author_email='marcello.debernardi@stcatz.ox.ac.uk',
    description='A library for approximating loss landscapes in low-dimensional parameter subspaces',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.5',
    install_requires=['numpy'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)