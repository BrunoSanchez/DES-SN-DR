from setuptools import find_packages, setup
# setup()
setup(
    name='dessndr',
    packages=find_packages(),
    version='0.1.0',
    description='The Dark Energy Survey Supernova 5YR Data Release',
    author='DES-SN',
    license='BSD-3',
    requires=['numpy', 'pandas', 'astropy']
)
