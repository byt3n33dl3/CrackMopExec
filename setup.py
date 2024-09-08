from setuptools import setup, find_packages
import re

VERSIONFILE="CrackMopExec/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
	# Application name:
	name="CrackMopExec",

	# Version number (initial):
	version=verstr,

	# Application author details:
	author="Tamas Jos",
	author="Sulaiman Aziz",
	author_email="info@skelsec.com",

	# Packages
	packages=find_packages(exclude=["tests*"]),

	# Include additional files into the package
	include_package_data=True,


	# Details
	url="https://github.com/pxcs/CrackMopExec",

	zip_safe = True,
	#
	# license="LICENSE.txt",
	description="Kerberos security toolkit for Python",

	# long_description=open("README.txt").read(),
	python_requires='>=3.6',
	classifiers=(
		"Programming Language :: Python :: 3.6",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	),
	install_requires=[
		'msldap>=0.4.7',
		'minikerberos>=0.4.0',
		'winsspi;platform_system=="Windows"',
		'winacl>=0.1.6; platform_system=="Windows"',
	],

	entry_points={
		'console_scripts': [
			'CrackMopExec = CrackMopExec.__main__:main',
		],
	}
)
