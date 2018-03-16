
import logging

__RESULT_ELEMENT_SELECTOR = "result_element_selector"


class search_result:

	__RESULT_URL_ELEMENT_SELECTOR = "result_url_element_selector"
	__RESULT_TITLE_ELEMENT_SELECTOR = "result_title_element_selector"
	__RESULT_SHOW_URL_ELEMENT_SELECTOR = "result_show_url_element_selector"
	__RESULT_SEM_ELEMENT_SELECTOR = "result_sem_element_selector"


	def __init__(self,config,element):
		self.element = element
		self.__result_title_element_selector = config.get(self.__RESULT_TITLE_ELEMENT_SELECTOR)
		self.__result_url_element_selector = config.get(self.__RESULT_URL_ELEMENT_SELECTOR)
		self.__result_show_url_element_selector = config.get(self.__RESULT_SHOW_URL_ELEMENT_SELECTOR)
		self.__result_sem_element_selector = config.get(self.__RESULT_SEM_ELEMENT_SELECTOR)

	def get_title(self):
		return self.element.find_element_by_css_selector(self.__result_title_element_selector)
	def get_url(self):
		return self.element.find_element_by_css_selector(self.__result_url_element_selector)

	def get_show_url(self):
		return self.element.find_element_by_css_selector(self.__result_show_url_element_selector)

	def is_sem(self):
		return self.element.find_element_by_css_selector(self.__result_sem_element_selector) != None

def parser(driver,config):

	result_element_selector = config.get(__RESULT_ELEMENT_SELECTOR)

	result_element_list = driver.find_elements_by_css_selector(result_element_selector)
	
	ret_list = []
	for result_element in result_element_list:
		ret = search_result(config,result_element)
		ret_list.append(ret)
#	return result_element_list
	return ret_list


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
