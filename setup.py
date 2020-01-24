from distutils.core import setup

setup(
    name='useeiopy',
    version='0.0.1',
    packages=['useeiopy'],
    package_data={'useeiopy': ["data/*.*"]},
    url='https://github.com/USEPA/useeiopy',
    license='CC0',
    author='Wesley Ingwersen',
    author_email='ingwersen.wesley@epa.gov',
    description='Assembles, calculates and writes out USEEIO environmentally-extended'
                'input-output models using the IO-Model-Builder.',
    install_requires=['iomb @ git+git://github.com/USEPA/IO-Model-Builder@v1.2.2#egg=iomb',
                      'appdirs>=1.3'],
    long_description = open('README.md').read(),
    classifiers = [
        "Development Status :: Alpha",
        "Environment :: IDE",
        "Intended Audience :: Science/Research",
        "License :: CC0",
        "Programming Language :: Python :: 3.x",
        "Topic :: Utilities",
    ],

)
