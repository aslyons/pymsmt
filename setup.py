
from distutils.core import setup
import os
import sys

# Packages in python MSMT toolbox
packages = ['api', 'mcpb', 'lib', 'msmtmol', 'ipmach']

# Modules
modules = ['pymsmtexp', 'title']

# Scripts
scripts = ['msmttools/MCPB.py', 'msmttools/OptC4.py', 'msmttools/PdbSearcher.py',
           'msmttools/espgen.py', 'msmttools/CartHess2FC.py', 'msmttools/IPMach.py',
           'msmttools/car2mol2.py']

if __name__ == '__main__':

    try:
        from distutils.command.build_py import build_py_2to3 as build_py
        from distutils.command.build_scripts import build_scripts_2to3 as build_scripts
        PY3 = True
    except ImportError:
        from distutils.command.build_py import build_py
        from distutils.command.build_scripts import build_scripts
        PY3 = False

    setup(name='pyMSMT',
          version='16.0', # For AmberTools 16
          description='Amber parameter file editor',
          author='Pengfei Li',
          author_email='ldsoar1990 -at- gmail.com',
          license='GPL v3 or later',
          packages=packages,
          py_modules=modules,
          cmdclass={'build_py':build_py, 'build_scripts':build_scripts},
          scripts=scripts)
