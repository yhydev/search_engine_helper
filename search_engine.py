#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from search_result import parser

class search_engine:
		
	__INPUT_ELEMENT_SELECTOR = "input_element_selector"
	__SUBMIT_ELEMENT_SELECTOR = "submit_element_selector"
	__SERACH_ENGINE_URL = "search_engine_url"

	

	
	def __init__(self,config):

		chrome_options = webdriver.ChromeOptions()
		prefs = {"profile.managed_default_content_settings.images":2}
		chrome_options.add_experimental_option("prefs",prefs)

		self.config = config	
		self.browser = webdriver.Chrome(chrome_options = chrome_options)
		self.browser.implicitly_wait(10)
		self.__search_engine_url = config.get(self.__SERACH_ENGINE_URL)
		self.__input_element_selector = config.get(self.__INPUT_ELEMENT_SELECTOR)
		self.__submit_element_selector = config.get(self.__SUBMIT_ELEMENT_SELECTOR)

		self.browser.get(self.__search_engine_url)
	
	def quit_browser(self):
		self.browser.quit()

	def search(self,word):
		
		input_element = self.browser.find_element_by_css_selector(self.__input_element_selector)
		input_element.clear()
		input_element.send_keys(word)
		

		submit_element = self.browser.find_element_by_css_selector(self.__submit_element_selector)
		submit_element.click()
		return parser(self.browser,self.config)
			
