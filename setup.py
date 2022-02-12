import sys
import pyminifier
from setuptools import setup
from distutils.command.install import INSTALL_SCHEMES

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']
    
from distutils.command.build_py import build_py

cmdclass = {'build_py': build_py}

setup(
    name="pyminifier",
    version=pyminifier.__version__,
    description="Python code minifier, obfuscator, and compressor",
    author=pyminifier.__author__,
    cmdclass=cmdclass,
    author_email="daniel.mcdougall@liftoffsoftware.com",
    url="https://github.com/liftoff/pyminifier",
    license="Proprietary",
    packages=['pyminifier'],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    provides=['pyminifier'],
    python_requires='>=3.6.2',
    entry_points = {
        'console_scripts': [
            'pyminifier = pyminifier.__main__:main'
        ],
    },
    test_suite = "tests",
)
