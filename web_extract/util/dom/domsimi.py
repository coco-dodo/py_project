#encoding:utf-8

from __future__ import division
from util.dom import minidom

def compute_simi(root1,root2):
	return nstm(root1,root2)

def stm(root1, root2):
	'''
		simple tree matching
		'''
	if not minidom.is_same(root1,root2):
		#_debug_print_return(0)
		return 0
	else:
		#k = the number of first-level sub-trees of A(root1)
	    #n = the number of first-level sub-trees of B(root2)
		k = minidom.element_child_count(root1)
		n = minidom.element_child_count(root2)

		#initialize the matrix m
		#m[i][0] <- 0 for 0...k ; m[0][j] <- 0...n
		m = [[0] * (n+1) for i in range(k+1)]

		#filling the matrix
		i = 1
		j = 1
		for subtree_a in minidom.element_child_iterator(root1):
			for subtree_b in minidom.element_child_iterator(root2):
	#			_debug_print_index(i,j)
				m[i][j] = max(m[i][j-1], m[i-1][j], m[i-1][j-1]+stm(subtree_a,subtree_b))
	#			_debug_print_matrix(m)
				j += 1
			i += 1
			j = 1

	#	_debug_print_return(m[k][n]+1)
		return m[k][n] + 1


def nstm(root1,root2):
	'''
		normalized simple tree matching 
		'''
	stm_cnt = stm(root1,root2)
	base_cnt = max(minidom.element_tree_count(root1),minidom.element_tree_count(root2))		
	# base_counts = (minidom.element_tree_count(root1) + minidom.element_tree_count(root2)) / 2
	return stm_cnt / base_cnt


def _debug_print_matrix(m):
	for row in m:
		record = ""
		for col in row:
			record += "%d\t" %col 
		print record

def _debug_print_index(i,j):
	print "(%d,%d)" %(i,j)

def _debug_print_return(rtn):
	print "return %d" %rtn 
	print "--------------"

