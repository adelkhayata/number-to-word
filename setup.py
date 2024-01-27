from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='number-to-word',
    version='1.0',
    packages=find_packages(),
    description='number-to-word is a Python library for converting numbers into their written English or Arabic word equivalents.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Adel Khayata',
    author_email='adel@khayata.com',
    url='https://github.com/adelkhayata/number-to-word',
    install_requires=[
        # List your package dependencies here
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
    license='MIT',
)
