#!/usr/bin/python

import os

def test_name(path):
	print "path : ", path, "dirname : %s" %os.path.dirname(path)
	print "path : ", path, "filename : %s" %os.path.basename(path)

def test_path(path):
	print "path : ", path, "abs path : %s" %os.path.abspath(path)
	print "path : ", path, "normal path : %s" %os.path.normpath(path)

def test_expanduser(path):
	print "path : ", path, "expand user path : %s" %os.path.expanduser(path)

def test_expandvars(path):
	os.environ["CLIPPER_HOME"] = "/home/qiaoyi/";
	print "path : ", path, "expand env var path : %s" %os.path.expandvars(path)

def test_pathjoin(parts):
	print "path parts : ",  parts, "join path : %s" %os.path.join(*parts)

def test_pathcommonprefix(paths):
	print "paths : ",  paths, "common prefix path : %s" %os.path.commonprefix(paths)

if(__name__ == "__main__"):
	test_name("~/works/py_project/udacity_crawler.py")
	test_path("~/works/../py_project/udacity_crawler.py")
	test_expanduser("~qiaoyi")
	test_expandvars("$CLIPPER_HOME")
	test_pathjoin(["/","qiaoyi","works","py_project"])
	test_pathcommonprefix(["/home/qiaoyi/","/home/qiaoyi/works/","/home/raymond"]);
	test_pathcommonprefix(["/home/qiaoyi/","/home/qiaoyi"]);
