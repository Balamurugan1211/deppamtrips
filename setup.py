from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in deppamtrips/__init__.py
from deppamtrips import __version__ as version

setup(
	name="deppamtrips",
	version=version,
	description="An app to create sales order from the tripsheet",
	author="bramachandran@techfinite.com",
	author_email="bramachandran@techfinite.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
