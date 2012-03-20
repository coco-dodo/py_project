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
#从xml string转换成xml element
def parse_string_to_element(xml_content):
	from elementtree.ElementTree import fromstring
	root = fromstring(xml_content)
	return root

#从xml filename 转换成xml element
def parse_file_to_element(xml_file_name):
	from elementtree.ElementTree import parse
	tree = parse(xml_file_name)
	root = tree.getroot()
	return root

#从root element开始 根据xml文档顺序遍历这棵xml子树
def doc_walk_iterator(root):
	return root.getiterator()

#广度优先遍历即树的层次遍历，使用队列数据结构
def bfs_walk_iterator(root):
	from collections import deque
	queue = deque();
	queue.append(root);
	while len(queue) > 0:
		next = queue.popleft()	
		yield next
		for child in list(next):
			queue.append(child)

#体会iterator的好处（generator yield）将处理逻辑从遍历中解耦，对于这种需要递归的遍历最能体现这个好处！！！
#中（只针对二叉树）/前/后根树的深度遍历 最简单使用递归算法
# 这里是前、后根深度遍历的例子
def dfs_walk_iterator(root):
	yield root #pre order
	from elementtree.ElementTree import Element
	for child in list(root):
		for next in dfs_walk_iterator(child):
			yield next
	#yield root	#post order

# 非递归 使用stack 中（只针对二叉树）/前/后根树的深度遍历 
def dfs_walk_iterator_v2(root):
	pass
	
if __name__ == "__main__":
	xml_file_name = "test.xml"
	root1 = parse_string_to_element(xml_content)
	root2 = parse_file_to_element(xml_file_name)
	for next in dfs_walk_iterator(root1):
		print next.tag
	for next in bfs_walk_iterator(root1):
		print next.tag
