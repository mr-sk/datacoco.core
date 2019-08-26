from distutils.core import setup
import os

VERSION = open("VERSION").readline().rstrip()

def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements

setup(
  name = 'datacoco.core',
  packages = ['datacoco.core'],
  version = VERSION,
  license='MIT',
  description = 'Core features of common code utility',
  author = 'Paul Singman',
  author_email = 'paul.singman@equinox.com',
  url = 'https://github.com/equinoxfitness/datacoco.core',
  download_url = 'https://github.com/equinoxfitness/datacoco.core/archive/0.1.tar.gz',
  keywords = ['helper', 'config', 'logging', 'common'],   # Keywords that define your package best
  install_requires=read_requirements()
)
