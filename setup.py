from distutils.core import setup

setup(
    name='useeiopy',
    version='0.0.0.1',
    packages=['useeiopy'],
    package_data={'useeiopy': ["data/*.*"]},
    url='https://github.com/USEPA/useeiopy',
    license='CC0',
    author='Wesley Ingwersen',
    author_email='ingwersen.wesley@epa.gov',
    description='Assembles, calculates and writes out USEEIO environmentally-extended'
                'input-output models using the IO-Model-Builder.',
    install_requires=['iomb>=1.2'],
    long_description = open('README.md').read(),
    classifiers = [
        "Development Status :: Alpha",
        "Environment :: IDE",
        "Intended Audience :: Science/Research",
        "License :: CC0",
        "Programming Language :: Python :: 3.x",
        "Topic :: Utilities",
    ],
    #This does not automatically install these dependencies
    dependency_links=['https://github.com/USEPA/IO-Model-Builder/archive/v1.2.zip']
)
