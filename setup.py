# setup.py

from setuptools import setup, find_packages

setup(
    name='corelogic-finance',
    version='1.0.0',
    description='Una librería robusta y precisa para cálculos financieros y de negocios.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='CoreLogic Dev Team',
    author_email='dev@corelogic.com',
    url='https://github.com/tu-usuario/corelogic-finance',
    # Busca automáticamente la carpeta 'corelogic'
    packages=find_packages(),
    # Dependencias del proyecto (deben coincidir con pyproject.toml)
    install_requires=[
        'numpy',
        'numpy-financial',
        'pandas',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    python_requires='>=3.11',
)