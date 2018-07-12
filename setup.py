from setuptools import setup, find_packages

setup(
    name='django-slugger',
    version='1.1.0',
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
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
