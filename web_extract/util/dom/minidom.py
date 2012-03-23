#encoding: utf-8
import html5lib
import xml.dom.minidom 
import xpath
from collections import deque

#Part A:规范化html
def formalize_html(_html):
	'''
		利用html5lib将html网页内容规范化后，返回规范xml
		'''
	doc = html5lib.parse(_html, treebuilder="dom")
	return doc.toxml()

#Part B:解析构造minidom的DOM树
def parse_xml_to_document(_xml):
	'''
		将xml string转换成minidom的DOM树
		'''
	doc = xml.dom.minidom.parseString(_xml.encode("utf-8"))
	return doc

def parse_xmlfile_to_document(file_name):
	'''
		将xml file转换成minidom的DOM树
		'''
	doc = xml.dom.minidom.parse(file_name)#or file object
	return doc

#Part C:xpath查询
def find_all_nodes_by_xpath(node, pattern):
	#context = xpath.XPathContext()
	#return context.find(pattern,node)
	return xpath.find(pattern,node)

def find_node_by_xpath(node, pattern):
	return xpath.findnode(pattern,node)
	#context = xpath.XPathContext()
	#return context.findnode(pattern,node)

#Part D:各种遍历
def postorder_dfs_walk_iterator(node):
	'''
		generator
		后续的深度优先遍历DOM树ELEMENT节点
		'''
	for child in node.childNodes:	
		if child.nodeType == child.ELEMENT_NODE:
			for next in postorder_dfs_walk_iterator(child):
				yield next
	yield node

def postorder_dfs_walk_iterator_v2(root):
	'''
		generator
		后续的深度优先遍历DOM树所有的节点
		'''
	for child in root.childNodes:	
		for next in postorder_dfs_walk_iterator_v2(child):
			yield next
	yield root

def bfs_walk_iterator(root):
	'''
		generator
		广度优先遍历DOM树ELEMENT节点
		'''
	queue = deque()
	if root.nodeType == root.ELEMENT_NODE:
		queue.append(root)
	while len(queue) > 0:
		next = queue.popleft()
		yield next
		for child in next.childNodes:
			if child.nodeType == child.ELEMENT_NODE:
				queue.append(child)
	
def element_child_iterator(parent):
	'''
		generator for element children
		遍历element儿子节点
		'''
	for child in parent.childNodes:
		if child.nodeType == child.ELEMENT_NODE:
			yield child

#Part E: 
def element_tree_count(root):
	'''
		dom 树element节点个数
		'''
	count = 0
	for next in bfs_walk_iterator(root):
		count += 1
	return count

def element_child_count(parent):
	'''
		parent 儿子element节点个数
		'''
	count = 0
	for child in element_child_iterator(parent):
		count += 1
	return count

#Part F: others utility fuctions
def is_same(node1, node2):
	'''
		以nodeName为依据判断两个node是否一样
		'''
	return node1.nodeName == node2.nodeName

def get_node_text(node):
	text = ""
	for next in postorder_dfs_walk_iterator_v2(node):
		if next.nodeType == next.TEXT_NODE:
			text += next.nodeValue
	return text


def test():
	_xml = '''
				<root>
					<tag1>
						<tag11></tag11>
						<tag12>
							tag12text
							<tag121>tag121text</tag121>
							<tag122>
								<tag1221></tag1221>
							</tag122>
							tag12text
						</tag12>
					</tag1>
					<tag2>
					</tag2>
					<tag3>
						tag3text
						<tag31></tag31>
					</tag3>
				</root>
			'''
#test parse
	doc = parse_xml_to_document(_xml)

#	doc = parse_xmlfile_to_document("1")

#	url = "http://blog.csdn.net/hengcai001/article/details/4166996";
#	page = fetcher.fetch_page(url);
#	page = formalize_html(page)
#	doc = parse_xml_to_document(page)

#test find
#	node = find_node_by_xpath(doc.documentElement, u"/html/body/")
#   print node.nodeName

#test walk
#	for next in postorder_dfs_walk_iterator(doc.documentElement):
#		print next.nodeName
	for next in bfs_walk_iterator(doc.documentElement):
		print "tag: %s  text : %s   len : %d" %(next.nodeName,get_node_text(next), len(get_node_text(next)))

if __name__ == "__main__":
	test()
