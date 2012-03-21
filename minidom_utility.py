#!/home/qiaoyi/python/bin/python
#encoding: utf-8
import html5lib
import xml.dom.minidom 
from xml.dom.minidom import parse, parseString
import xpath
import fetcher

#Part A:解析构造minidom的DOM树
def parse_html_to_document(_html):
	'''
		利用html5lib将html网页内容规范化后，转换成minidom的DOM树
		'''
	doc = html5lib.parse(_html, treebuilder="dom")
	return doc

def parse_xml_to_document(_xml):
	'''
		将xml string转换成minidom的DOM树
		'''
	doc = xml.dom.minidom.parseString(_xml)
	return doc

def parse_xmlfile_to_document(file_name):
	'''
		将xml file转换成minidom的DOM树
		'''
	doc = parse(file_name)#or file object
	return doc

#Part B:xpath查询
def find_all_nodes_by_xpath(node, pattern):
	context = xpath.XPathContext()
	return context.find(pattern,node)

def find_node_by_xpath(node, pattern):
	context = xpath.XPathContext()
	return context.findnode(pattern,node)

def test():
	_xml = '''
				<root>
					<tag1>
						<tag11></tag11>
						<tag12>
							<tag121></tag121>
							<tag122>
								<tag1221></tag1221>
							</tag122>
						</tag12>
					</tag1>
					<tag2>
					</tag2>
					<tag3>
						<tag31></tag31>
					</tag3>
				</root>
			'''
#	doc = parse_xml_to_document(_xml)
	url = "http://www.baidu.com/s?wd=site%3Asearch.china.alibaba.com";
	page = fetcher.get_page(url);
	doc = parse_html_to_document(page)	
#	doc = parse_xmlfile_to_document("1")
	node = find_node_by_xpath(doc.documentElement, u"./body[1]/div[1]/div[1]/div[1]/div[1]/a[1]")

	print node.nodeName

if __name__ == "__main__":
	test()
