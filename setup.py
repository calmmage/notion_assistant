#!/usr/bin/env python

import re
from distutils.core import setup
from pathlib import Path

VERSIONFILE = Path("notion_assistant/_version.py")
verstrline = VERSIONFILE.read_text()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
      raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(name='Notion Assistant',
      version=verstr,
      description='Notion Assistant: Jarvis',
      author='Petr Lavrov, Aleksei Kudrinskii',
      author_email='calmquant@gmail.com',
      url='https://github.com/calmquant/notion_assistant',
      packages=['notion_assistant'],
      long_description=Path('README.md').read_text(),
      install_requires=Path('requirements.txt').read_text().split()
      )
