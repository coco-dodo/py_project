#!/home/qiaoyi/python/bin/python
#coding=utf-8
import urllib
import md5
import chardet

def cbk(a, b, c):  
    per = 100.0 * a * b / c  
    if per > 100:  
        per = 100  
    print 'fetch page progress :  %.2f%%' % per  


def fetch_page_by_proxy(url):
	wk_render_proxy_host = "10.20.150.83"
	wk_render_proxy_port = "20004"
	params = urllib.urlencode({"url":url})
	wk_render_proxy = "http://%s:%s/api/pageloader-nojs?%s" %(wk_render_proxy_host, wk_render_proxy_port, params)

	return urllib.urlopen(wk_render_proxy).read()
	
def fetch_page(url):
	print md5.new(url).digest().encode("UTF-8")
	return urllib.urlopen(url).read()
	

if __name__ == "__main__":
	pass
