#!/home/qiaoyi/python/bin/python
#encoding:utf-8
from extractor import template_extractor
from util.dom import minidom

if __name__ == "__main__":
	#input url template_id
	url = "http://developer.yahoo.com/python/python-xml.html"
	template_id = "290";
	#load web page
	page = template_extractor.load_page(url)
	formal_page = minidom.formalize_html(page)	
	doc = minidom.parse_xml_to_document(formal_page)
	#load template
	template = template_extractor.load_template(template_id)
	#do extract
	result = template_extractor.extract(doc, template)

	print result

