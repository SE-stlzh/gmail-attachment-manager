"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['gam.py']
DATA_FILES = ['client_secret.json','gmail.storage','gamil_t0.storage','gamil_t1.storage','gamil_t2.storage','gamil_t3.storage','mail.json']

OPTIONS = {'argv_emulation': False,
           'packages': ['httplib2','PyQt4'],
           'includes': ['httplib2','PyQt4','apiclient','oauth2client']}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
