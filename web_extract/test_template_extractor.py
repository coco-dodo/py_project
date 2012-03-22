#!/home/qiaoyi/python/bin/python
#encoding:utf-8
from extractor import template_extractor
from util.dom import minidom

def do_template_extract(url, template_id):
	#load web page
	page = template_extractor.load_page(url)
	formal_page = minidom.formalize_html(page)	
	doc = minidom.parse_xml_to_document(formal_page)
	
	#load template
	template = template_extractor.load_template(template_id)
	
	#do extract
	page_result = template_extractor.extract(doc, template)

	#print result
	print "page url:%s" %url
	print "extract result:-------"
	for field_result in page_result:
		print field_result
	print "----------------------"


if __name__ == "__main__":
	#input url template_id
	urls = [
				"http://www.oschina.net/news/27069/5-technics-for-bigdata-analysis",
				"http://www.oschina.net/news/27070/druid-0-2",
				"http://www.oschina.net/news/27066/ueditor-1-2-0-final",
				"http://www.oschina.net/news/27064/firefox-descend",
				"http://www.oschina.net/news/27059/safe-web",
				]
	template_id = "295";

	for url in urls:
		do_template_extract(url,template_id)	


