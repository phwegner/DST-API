from setuptools import setup

setup(name='dstapi',
      version='0.1',
      description='',
      url='https://gitlab.scai.fraunhofer.de/philipp.wegner/dst-api',
      author='Philipp Wegner',
      author_email='philipp.wegner@scai.fraunhofer.de',
      license='MIT',
      packages=['dstapi'],
      install_requires=[
          'requests', 
          'dataclasses'
      ],
      zip_safe=False)