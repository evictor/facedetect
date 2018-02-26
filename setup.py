from setuptools import setup

setup(name='facedetect',
      version='0.2',
      description='a simple face detector for batch processing - https://www.thregr.org/~wavexx/software/facedetect/',
      url='https://github.com/wavexx/facedetect',
      author='Yuri D\'Elia',
      license='GPL v2',
      packages=['facedetect'],
      zip_safe=True,
      install_requires=['numpy', 'opencv-python'])
