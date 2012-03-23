#!/home/qiaoyi/python/bin/python
#encoding:utf-8

from util.dom import domsimi
from util.dom import minidom

_html1 = '''
				<body>
					<div>
						<div></div>
					</div>
					<div>
						<font></font>
						<p>
							<a></a>
						</p>
					</div>
					<p>
						<a></a>
					</p>
				</body>
			'''
_html2 = '''
				<body>
					<div>
						<span></span>
					</div>
					<div>
						<p></p>
					</div>
					<table>
						<tr></tr>
						<tr></tr>
					</table>
					<p></p>
				</body>
			'''
def test_dom_simi():
	doc1 = minidom.parse_xml_to_document(_html1)	
	doc2 = minidom.parse_xml_to_document(_html2)	

	#domsimi.stm(doc1.documentElement,doc2.documentElement)	
	#print domsimi.nstm(doc1.documentElement,doc2.documentElement)
	print domsimi.compute_simi(doc1.documentElement,doc2.documentElement)
if __name__ == "__main__":
	test_dom_simi()
