from setuptools import setup, find_packages

# Read requirements.txt and install
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='GDPGoogleConnector',
    version='1.0.0',
    description='A utility class for managing Google Apps Script executions via Python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=requirements,
    python_requires='>=3.6'
)
