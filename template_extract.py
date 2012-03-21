#!/home/qiaoyi/python/bin/python
#coding:UTF-8 
import db_utility
import fetcher
import json
import minidom_utility
import chardet
import sys 

def load_template(template_id):
	conn = db_utility.mysql_connect("10.20.150.83",3307,"pca","pca","clipper")	
	records = db_utility.mysql_query(conn,"select content from template where id=%s",template_id)
	db_utility.mysql_close(conn)
	if len(records) > 0:
		return json.loads(records[0][0])
	else:
		return

def load_page(url):
	page_file = fetcher.get_page(url)
	#encoding_info = chardet.detect(raw_page)
	#page = raw_page.decode(encoding_info["encoding"]).encode("UTF-8")
	#page = raw_page.decode("GBK").encode("UTF-8")
	#return page 
	return page_file

def postorder_dfs_walk_iterator(root_field):
	for child_field in root_field["children"]:
		for next in postorder_dfs_walk_iterator(child_field):
			yield child_field
	yield root_field

def one_level_walk_iterator(root_field):
	for child_field in root_field["children"]:
		yield child_field

def extract(doc, template):

	#iterator extract field in the templates
	for field in one_level_walk_iterator(template["root_field"]):

		#locate the extract field node using field xpath location
		field_xpath = field["location"]["start_xpath"]
		field_xpath = "." + field_xpath[field_xpath.find("html[1]")+len("html[1]"):]
		field_element = minidom_utility.find_node_by_xpath(doc.documentElement,field_xpath)

		if field_element is None:
			print "cannot locate the field element"
			print "field xpath : %s" %field_xpath
		else:
			#do the extract work
			print field_element
			pass

if __name__ == "__main__":
	url = "http://www.baidu.com/s?wd=site%3Asearch.china.alibaba.com";
	page = load_page(url);
	doc = minidom_utility.parse_html_to_document(page)	
#	doc = minidom_utility.parse_xmlfile_to_document("1") #TODO

	template_id = "286";
	template = load_template(template_id)

	extract(doc, template)

