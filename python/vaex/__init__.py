"""
Vaex is...
"""# -*- coding: utf-8 -*-
try:
	import version
except:
	import sys
	print >>sys.stderr, "version file not found, please run git/hooks/post-commit or git/hooks/post-checkout and/or install them as hooks (see git/README)"
	raise

__release_name__ = "alpha"
__version_tuple__ = version.versiontuple
__program_name__ = "vaex"
__version__ = "%d.%d.%d" % __version_tuple__
__release__ = version.versiontring[:]
__clean_release__ = "%d.%d.%d" % (__version_tuple__)
__full_name__ = __program_name__ + "-" + __release__
__clean_name__ =  __program_name__ + "-" + __clean_release__

import vaex.dataset
#import vaex.plot

def open(path, *args, **kwargs):
	"""Open a dataset from file given by path

	:param str path: local or absolute path to file
	:param args: extra arguments for file readers that need it
	:param kwargs: extra keyword arguments
	:return: return dataset if file is supported, otherwise None
	:rtype: vaex.dataset.Dataset

	:Example:

	>>> import vaex as vx
	>>> vx.open('myfile.hdf5')
	<vaex.dataset.Hdf5MemoryMapped at 0x1136ee3d0>
	>>> vx.open('gadget_file.hdf5', 3) # this will read only particle type 3
	<vaex.dataset.Hdf5MemoryMappedGadget at 0x1136ef3d0>
	"""
	return vaex.dataset.load_file(path, *args, **kwargs)

def server(hostname, **kwargs):
	"""Connect to hostname supporting the vaex web api

	:param str hostname: hostname or ip address of server
	:return vaex.dataset.ServerRest: returns a server object, note that it does not connect to the server yet, so this will always succeed
	:rtype: vaex.dataset.ServerRest
	"""
	return vaex.dataset.ServerRest(hostname, **kwargs)

def example():
	"""Returns an example dataset which comes with vaex for learning purposes

	:rtype: vaex.dataset.Dataset
	"""
	import utils
	return open(utils.get_data_file("helmi-dezeeuw-2000-10p.hdf5"))


def set_log_level_debug():
	import vaex.logging as log
	log.rootlogger.setLevel(log.LEVELS['debug'])

def set_log_level_info():
	import vaex.logging as log
	log.rootlogger.setLevel(log.LEVELS['info'])

def set_log_level_warning():
	import vaex.logging as log
	log.rootlogger.setLevel(log.LEVELS['warning'])