"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Pinger.py']
DATA_FILES = []
OPTIONS = {
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps', 'pkg_resources'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)