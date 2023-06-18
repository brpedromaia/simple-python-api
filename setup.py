from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='python-api',
   version='1.0',
   description='A useful module',
   license="MIT",
   long_description=long_description,
   author='Man Foo',
   author_email='foomail@foo.example',
   url="http://www.foopackage.example/",
   packages=['src'],  #same as name
   install_requires=[
          'fastapi',
          'uvicorn',
          'SQLAlchemy',
          'elastic-apm',
                    ], #external packages as dependencies
#    scripts=[
#             'scripts/test1',
#             'scripts/test2',
#            ]
)