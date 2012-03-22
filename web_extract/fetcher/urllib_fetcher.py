#coding=utf-8
import urllib
import chardet

def cbk(a, b, c):  
    per = 100.0 * a * b / c  
    if per > 100:  
        per = 100  
    print 'fetch page progress :  %.2f%%' % per  

def fetch_page_by_proxy(url):
	'''
		download page using webkit render service
		'''
	wk_render_proxy_host = "10.20.150.83"
	wk_render_proxy_port = "20004"
	params = urllib.urlencode({"url":url})
	wk_render_proxy = "http://%s:%s/api/pageloader-nojs?%s" %(wk_render_proxy_host, wk_render_proxy_port, params)

	return urllib.urlopen(wk_render_proxy).read()
	
def fetch_page(url):
	'''
		download page
		'''
	return  urllib.urlopen(url).read()
	
def test():
	page = fetch_page("http://www.iteye.com/topic/561786")
	encoding = chardet.detect(page)
	print page
	print encoding

if __name__ == "__main__":
	test()
