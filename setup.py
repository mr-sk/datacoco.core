from distutils.core import setup
import os

def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements

setup(
  name = 'cocore',
  packages = ['cocore'],
  version = VERSION,
  license='MIT',
  description = 'Core features of common code utility',
  author = 'Paul Singman',
  author_email = 'paul.singman@equinox.com',
  url = 'https://github.com/equinoxfitness/datacoco.core',
  download_url = f'https://github.com/equinoxfitness/datacoco.core/archive/0.4.tar.gz',
  keywords = ['helper', 'config', 'logging', 'common'],   # Keywords that define your package best
  install_requires=read_requirements()
)
