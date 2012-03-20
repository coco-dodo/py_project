#!/usr/bin/python
#--*-- encoding:utf-8 --*--
xml_content = '''
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
def parse_string_to_element(xml_content):
	'''
		从xml string转换成xml element
		'''
	from elementtree.ElementTree import fromstring
	root = fromstring(xml_content)
	return root

def parse_file_to_element(xml_file_name):
	'''
		从xml filename 转换成xml element
		'''
	from elementtree.ElementTree import parse
	tree = parse(xml_file_name)
	root = tree.getroot()
	return root

def doc_walk_iterator(root):
	'''
		从root element开始 根据xml文档顺序遍历这棵xml子树
		'''
	return root.getiterator()

def bfs_walk_iterator(root):
	'''
		广度优先遍历即树的层次遍历，使用队列数据结构
		'''
	from collections import deque
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
	from elementtree.ElementTree import Element
	for child in list(root):
		for next in dfs_walk_iterator(child):
			yield next
	#yield root	#post order

def dfs_walk_iterator_v2(root):
	'''
		非递归 使用stack 中（只针对二叉树）/前/后根树的深度遍历 
		'''
	pass
	
def compute_similarity(root_one,root_second):
	pass




if __name__ == "__main__":
	xml_file_name = "test.xml"
	root1 = parse_string_to_element(xml_content)
	root2 = parse_file_to_element(xml_file_name)
	for next in dfs_walk_iterator(root1):
		print next.tag
	for next in bfs_walk_iterator(root1):
		print next.tag
