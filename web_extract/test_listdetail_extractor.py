#!/home/qiaoyi/python/bin/python
#encoding:utf-8

from extractor import listdetail_extractor
from util.dom import minidom

if __name__ == '__main__':
#	url = "http://www.oschina.net/news"
#	url = "http://mobile.taobao.com/list.htm?spm=1.151826.185134.5&cat=1512&pidvid=20000%3A33564%3B30606%3A3271031%2C10285019%2C11397753&sort=_sd_quantity#items"
#	url = "http://www.360buy.com/brands/832-7.html"
#	url = "http://list.taobao.com/market/shuma.htm?cat=1512&sort=coefp&viewIndex=17&yp4p_page=0&commend=all&style=list&q=iphone&ppath=20573%3A48200#J_Filter"
	url = "http://list.tmall.com/search_product.htm?q=ipad&commend=all&ssid=s5-e&search_type=mall&sourceId=tb.index&initiative_id=tbindexz_20120323&prt=1332488471746&prc=1"
	listdetail_extractor.extract(url)
