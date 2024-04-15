#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, Extension
import os
import sys
import platform
import glob

os.environ['NPY_DISTUTILS_APPEND_FLAGS'] = '1'

if platform.system() == 'Windows':
    # For Anaconda
    cflags = ['-O1', '-m64', '-fPIC', '-std=c99','-DCMINPACK_NO_DLL']
elif sys.platform == 'cygwin':
    cflags = ['-O1', '-m64', '-fPIC', '-std=c99']
elif platform.system() == 'Darwin':
    cflags = ['-O1', '-m64', '-fno-omit-frame-pointer', '-fPIC']#, '-std=c99']
else:
    #cflags = ['-O1', '-m64', '-fPIC', '-std=c99', '-D WITH_LAPACK']
    cflags = ['-O1', '-m64', '-fPIC', '-std=c99']

pymapExt   = Extension('pymap._libmap',
                       sources=glob.glob(os.path.join('pymap','src','**','*.c'), recursive=True)+
                       glob.glob(os.path.join('pymap','src','**','*.cc'), recursive=True),
                       extra_compile_args=cflags,
                       include_dirs=[os.path.join('pymap','src','lapack')])
    
setup(
    ext_modules=[pymapExt],
)


