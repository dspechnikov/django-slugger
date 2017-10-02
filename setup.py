from setuptools import setup, find_packages

__version__ = '1.0.1'

setup(
    name='django-slugger',
    version=__version__,
    url='https://gitlab.com/dspechnikov/django-slugger/',
    description='Automatic slug field for Django.',
    license='MIT',

    author='Dmitry Pechnikov',
    author_email='dspechnikov@gmail.com',

    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'django',
        'unidecode',
    ],

    long_description=open('README.rst').read(),
    keywords='django field slug auto',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
