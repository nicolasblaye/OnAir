from setuptools import setup

setup(
    name='On Air',
    packages=['on_air'],
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-Script'
    ],
)