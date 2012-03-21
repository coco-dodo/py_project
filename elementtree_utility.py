#!/home/qiaoyi/python/bin/python
#--*-- encoding:utf-8 --*--
import html5lib
from elementtree.ElementTree import Element
from collections import deque

#Part A: 利用html5lib规范化html,然后构造elementtree dom树
def parse_html_to_tree(html):
	'''
		利用html5lib模块规范化html文档内容，从html转换成xml element dom tree
		'''
	root = html5lib.parse(html, treebuilder="etree")	
	return root
	
def parse_htmlfile_to_tree(file_name):
	'''
		利用html5lib模块规范化html文档内容，从html file 转换成xml element dom 树
		'''
	root = html5lib.parse(file_name, treebuilder="etree")	
	return root 

def parse_xml_to_tree(xml):
	'''
		从xml string 构造elementtree dom树
		'''
	root = fromstring(xml_content)
	return root

def parse_xmlfile_to_tree(xml):
	'''
		从xml file 构造elementtree dom树
		'''
	tree = parse(xml_file_name)
	return tree

#Part B: 遍历操作
def doc_walk_iterator(root):
	'''
		从root element开始 根据xml文档顺序遍历这棵xml子树
		'''
	return root.getiterator()

def bfs_walk_iterator(root):
	'''
		广度优先遍历即树的层次遍历，使用队列数据结构
		'''
	queue = deque();
	queue.append(root);
	while len(queue) > 0:
		next = queue.popleft()	
		yield next
		for child in list(next):
			queue.append(child)

def dfs_walk_iterator(root):
	'''
		体会iterator的好处（generator yield）将处理逻辑从遍历中解耦，对于这种需要递归的遍历最能体现这个好处！！！
		中（只针对二叉树）/前/后根树的深度遍历 最简单使用递归算法
		这里是前、后根深度遍历的例子
		'''
	yield root #pre order
	for child in list(root):
		for next in dfs_walk_iterator(child):
			yield next
	#yield root	#post order

def dfs_walk_iterator_v2(root):
	'''
		非递归 使用stack 中（只针对二叉树）/前/后根树的深度遍历 
		'''
	pass
	
#Part C:
def find_element_by_pattern(element, pattern):
	return element.find(pattern)

def compute_similarity(root_one,root_second):
	pass




if __name__ == "__main__":
	pass
