
import logging

__RESULT_ELEMENT_SELECTOR = "result_element_selector"


class search_result:

	__RESULT_URL_ELEMENT_SELECTOR = "result_url_element_selector"
	__RESULT_TITLE_ELEMENT_SELECTOR = "result_title_element_selector"
	__RESULT_SHOW_URL_SELECTOR = "result_show_url_selector"



	def __init__(self,element,config):
		self.element = element
		self.result_title_element_selector = config.get(self.__RESULT_TITLE_ELEMENT_SELECTOR)
		self.result_url_element_selector = config.get(self.__RESULT_URL_ELEMENT_SELECTOR)
		self.result_show_url_selector = config.get(self.__RESULT_SHOW_URL_SELECTOR)
	

	def get_title():
		return element.find_element_by_css_selector(self.result_title_element_selector)
	def url():
		return element.find_element_by_css_selector(self.result_url_element_selector)

	def show_url():
		return element.find_element_by_css_selector(self.result_show_url_selector)

def parser(driver,config):

	result_element_selector = config.get(__RESULT_ELEMENT_SELECTOR)

	result_element_list = driver.find_elements_by_css_selector(result_element_selector)
	print result_element_list
	result_list = []

	for result_element in result_element_list:

		search_re = search_result(result_element,config)
		result_list.append(search_re)

	return result_list	

def parses(page_source,config):
	
	logging.info("selector element info:" )
	
	logging.info(config)
	
	logging.info("page parseing ..")

	doc = PyQuery(page_source)

	result_title_element_selector = config.get(__RESULT_TITLE_ELEMENT_SELECTOR)
	result_url_element_selector = config.get(__RESULT_URL_ELEMENT_SELECTOR)
	result_element_selector = config.get(__RESULT_ELEMENT_SELECTOR)

	result_element_list = doc(result_element_selector)

	
	re_html = open("re.html","w") 
	re_html.write(page_source)
	re_html.close()



	search_result_list = []

	for result_element in result_element_list:
		
		url = result_element(result_url_element_selector)
		title = result_element(result_title_element_selector)
		show_url = result_element(result_show_url_selector)	
		
		search_result = search_result_list(url,title,show_url)
		search_result_list.append(search_result)
	
	return search_result_list
