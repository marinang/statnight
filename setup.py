#!/usr/bin/python

import sys
import os.path

from setuptools import find_packages
from setuptools import setup

major, minor = sys.version_info[:2]

tr = ["pytest","jupyter", "papermill"]

if major >= 3 and minor >= 5:
	ir = ["iminuit", "numpy", "scipy", "matplotlib"]
else:
	ir = ["iminuit", "numpy", "scipy", "matplotlib<3.0"]
	
if major == 3 and minor == 2:
	tr.append("attrs==17.4.0")
	tr.append("jsonschema>=v3.0.0a2")
elif major == 2 and minor == 7:
	tr.append("ipykernel<5.1.0")
	
if major >= 3 and minor > 4:
	pass
else:
	tr.append("ipython<6.0")


setup(  name = "statnight",
	version = "1.0",
	packages = find_packages(exclude = ["tests"]),
	scripts = [],
	data_files = ["README.md"],
	description = "Pure python statistic tools for high energy physics, based on iminuit.",
	long_description = "",
	author = "Matthieu Marinangeli",
	author_email = "matthieu.marinangeli@epfl.ch",
	maintainer = "Matthieu Marinangeli",
	maintainer_email = "matthieu.marinangeli@epfl.ch",
	url = "https://github.com/marinang/statrise",
	download_url = "",
	license = "",
	test_suite = "tests",
	install_requires = ir,
	setup_requires = ["pytest-runner"],
	tests_require = tr,
	classifiers = [
			"Intended Audience :: Science/Research",
			"Operating System :: MacOS",
			"Operating System :: POSIX",
			"Operating System :: Unix",
			"Programming Language :: Python",
			"Programming Language :: Python :: 3.4",
			"Programming Language :: Python :: 3.5",
			"Programming Language :: Python :: 3.6",
			"Programming Language :: Python :: 3.7",
			"Topic :: Scientific/Engineering :: Physics",
			],
	platforms = "Any",
		)
		