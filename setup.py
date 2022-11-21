from setuptools import setup

setup(
    name='yumiriam_gh_page',
    version='1.0',
    description='My personal page at Github',
    author='Miriam Yumi',
    author_email='miriamyume@gmail.com',
    packages=['source'],
    install_requires=[
        'sphinx',
        'ablog',
        'pydata-sphinx-theme',
        'sphinx-panels',
        'sphinx-icon',
    ],
)

