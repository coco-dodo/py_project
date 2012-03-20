#!/usr/bin/python

import urllib
def cbk(a, b, c):  
    per = 100.0 * a * b / c  
    if per > 100:  
        per = 100  
    print '%.2f%%' % per  


def get_page(url,page):
	wk_render_proxy_host = "10.20.150.83"
	wk_render_proxy_port = "20004"
	params = urllib.urlencode({"url":url})
	wk_render_proxy = "http://%s:%s/api/pageloader-nojs?%s" %(wk_render_proxy_host, wk_render_proxy_port, params)

	page = urllib.urlopen(wk_render_proxy)
	
	print urllib.urlretrieve(wk_render_proxy,"page",cbk)
	
if __name__ == "__main__":
	page = ""
	get_page("http://www.baidu.com",page)
