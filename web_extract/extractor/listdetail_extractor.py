#encoding:utf-8
from util.dom import minidom
from util.dom import domsimi
from fetcher import urllib_fetcher

def load_page(url):
	raw_page = urllib_fetcher.fetch_page(url)
	return raw_page

def get_list_candidate_nodes(doc):
	'''
		find all the list candidate nodes in the web page dom tree
		'''
	list_candidate_nodes = []

	#dfs walk web page dom tree
	for next in minidom.postorder_dfs_walk_iterator(doc.documentElement):
		list_item_candidate_nodes = []

		for child in minidom.element_child_iterator(next):
			if len(list_item_candidate_nodes) == 0:
				list_item_candidate_nodes.append(child)
			else:
				#compute similarity with siblings
				last = list_item_candidate_nodes[len(list_item_candidate_nodes) - 1]
				simi_score = domsimi.compute_simi(last, child)

				#judge if it's a listitem candidate
				if simi_score > 0.8 :
					list_item_candidate_nodes.append(child)

		#judge if it's a list candidate	
		if len(list_item_candidate_nodes) > 4:
			list_candidate_node_info = {"list":next,"items":list_item_candidate_nodes}
			list_candidate_nodes.append(list_candidate_node_info)
	
	return list_candidate_nodes

def get_list_node(list_candidate_nodes):
	'''
		find the most important list candidate node, return it as the result list node
		the importance is measured using node text length
		'''
	for candidate in list_candidate_nodes:
		candidate["length"] = len(minidom.get_node_text(candidate["list"]))

	list_candidate_nodes = \
		sorted(list_candidate_nodes, cmp = lambda x,y: cmp(x["length"],y["length"]), key = lambda x : x, reverse = True)

	if len(list_candidate_nodes) > 0:
		return list_candidate_nodes[0]
	else:
		return None

def get_list_item_info(list_node):
	'''
		get the wanted info in the list item
		'''
	list_item_infos = []
	# the wanted info: the most valuable outlink
	for list_item_node in list_node["items"]:
		#get all the anchors
		anchors = minidom.find_all_nodes_by_xpath(list_item_node,".//a")	
		max_length = 0
		important_anchor = ""
		for anchor in anchors:
			#return the anchor whose anchor text length is the longest
			if len(minidom.get_node_text(anchor)) > max_length:
				max_length = len(minidom.get_node_text(anchor))	
				important_anchor = anchor.getAttribute("href")
				#important_anchor = anchor.toxml()
				list_item_infos.append(important_anchor)
	
	#the wanted info: the most valuable text info

	return list_item_infos

def extract(url):
	#load web page
	page = load_page(url)
	formal_page = minidom.formalize_html(page)	
	doc = minidom.parse_xml_to_document(formal_page)

	#get list candidate nodes
	list_candidate_nodes = get_list_candidate_nodes(doc) 

	#get one list node which is judged as the most important list
	list_node = get_list_node(list_candidate_nodes)

	#get the need list item infos
	list_item_infos =get_list_item_info(list_node)

	#print extract info
	print "page url : %s" %url
	print "extract list item infos : "
	for info in list_item_infos:
		print info
	print "-------------"
