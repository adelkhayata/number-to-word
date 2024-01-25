from setuptools import setup, find_packages

setup(
    name='number-to-word',
    version='0.1',
    packages=find_packages(),
    description='number-to-word is a Python library for converting numbers into their written English or Arabic word equivalents.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Adel Khayata',
    author_email='adel@khayata.com',
    url='https://github.com/adelkhayata/number-to-word',
    install_requires=[
        # List your package dependencies here
    ],
)
