from distutils.core import setup

# Keeping all Python code for package in lib directory
NAME = 'cplate'
VERSION = '0.1'
AUTHOR = 'Alexander W Blocker'
AUTHOR_EMAIL = 'ablocker@gmail.com'
URL = 'http://www.awblocker.com'
DESCRIPTION = 'Probablistic deconvolution for chromatin-structure estimation.'

REQUIRES = ['numpy(>=1.6)','scipy(>=0.9)', 'yaml', 'mpi4py']

PACKAGE_DIR = {'': 'lib'}
PACKAGES = ['cplate']
SCRIPTS = ('deconvolve_em', 'deconvolve_mcmc', 'detect_em', 'summarise_mcmc')
SCRIPTS = ['scripts/cplate_' + script for script in SCRIPTS]

setup(name=NAME,
      url=URL,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      packages=PACKAGES,
      package_dir=PACKAGE_DIR,
      scripts=SCRIPTS,
      requires=REQUIRES
      )
