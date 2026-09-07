from setuptools import setup

setup(
    name='dataclassy',
    version='2.0.0',

    author='biqqles',
    author_email='biqqles@proton.me',
    url='https://github.com/biqqles/dataclassy',

    description='A fast and flexible reimplementation of data classes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    packages=['dataclassy'],
    package_data={
        'dataclassy': ['py.typed'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Typing :: Typed',
    ],
    python_requires='>=3.6',
)
