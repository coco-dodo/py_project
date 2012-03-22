#encoding: utf-8 
import json
import chardet
import sys 

from util.db import mysql
from util.dom import minidom 
from fetcher import urllib_fetcher

def load_template(template_id):
	conn = mysql.mysql_connect("10.20.150.83",3307,"pca","pca","clipper")	
	records = mysql.mysql_query(conn,"select content from template where id=%s",template_id)
	mysql.mysql_close(conn)
	if len(records) > 0:
		return json.loads(records[0][0].decode(chardet.detect(records[0][0])['encoding']))
	else:
		return

def load_page(url):
	raw_page = urllib_fetcher.fetch_page(url)
	return raw_page

def postorder_dfs_walk_iterator(root_field):
	for child_field in root_field["children"]:
		for next in postorder_dfs_walk_iterator(child_field):
			yield child_field
	yield root_field

def one_level_walk_iterator(root_field):
	for child_field in root_field["children"]:
		yield child_field

def do_extract_work(field, field_element):
	#get field_element text value
	text = field_element.childNodes[0].nodeValue
	return text

	#get field_element href attr value
	#TODO
	pass

def extract(doc, template):
	'''
		extract page content by template
		input: 1)xml.dom.minidom; 2)template
		output: 1)extract result
		'''
	result = []
	#iterator extract field in the templates
	for field in one_level_walk_iterator(template["root_field"]):
		#locate the extract field node using field xpath location
		field_xpath = field["location"]["start_xpath"]
		field_element = minidom.find_node_by_xpath(doc.documentElement,field_xpath)

		if field_element is None:
			print "cannot locate the field element"
			print "field xpath : %s" %field_xpath
		else:
			#do the extract work
			extract_value = do_extract_work(field,field_element)
			extract_key = field["name"]
			field_extract_result = "[%s] : [%s]" %(extract_key,extract_value)
			result.append(field_extract_result)
	return result

