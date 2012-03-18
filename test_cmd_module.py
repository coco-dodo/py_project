#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import cmd

class SerachingTool(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = "(SerachingToolPrompt)>"
		self.intro = '''SerachingTool usage:.....
						'''
	def help_EOF(self):
		print u"Quits the program!";
	def do_EOF(self,line):
		sys.exit();

	def help_dir(self):
		print u"specify the walk root dir!";
	def do_dir(self, pathname):
		if pathname == "":
			pathname = raw_input("walk root dir:")
		print "walk root dir %s" %pathname
		#TODO to implement the real logic
		pass

	def help_walk(self):
		print "walk all the dir files / subdirs and export into '.content' "
	def do_walk(self, filename):
		if filename == "":
			filename = raw_input("input .content file name:")
		print "walk and export content to file %s" %filename
		#TODO to implement the real logic
		pass

	def help_find(self):
		print "specify the finding keyword "
	def do_find(self, keyword):
		if keyword == "":
			keyword = raw_input("input the searching keyword:")
		print "the searching keyword is %s" %keyword
		#TODO to implement the real logic
		pass



if __name__ == "__main__":
	st = SerachingTool()
	st.cmdloop()

