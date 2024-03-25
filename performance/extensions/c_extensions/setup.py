from distutils.core import setup, Extension

module = Extension('example', sources = ['example.c'])

setup(name='Example',
      version='1.0',
      description='Python Package with a C Extension',
      ext_modules=[module])
