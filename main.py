#!/usr/bin/python
# -*- coding: utf-8 -*-

from search_engine import search_engine
import ConfigParser,logging
import sys,re

reload(sys)
sys.setdefaultencoding("utf8")

def get_configs():
	config_parser = ConfigParser.ConfigParser()
	config_parser.read("config.ini")	
	sections = config_parser.sections()

	configs = [];
	
	for section in sections:
		config =  config_parser.items(section)
		config_dict = {}
		for (n,v) in config:
			config_dict[n] = v
	
		configs.append(config_dict)
	
	return configs;


if __name__ == '__main__':

		logging.getLogger().setLevel(logging.INFO)

		configs = get_configs()

		baidu = search_engine(configs[0])

		result_list = baidu.search(u'\u6c47\u901a\u671f\u8d27')
		for result in result_list:

			try:
				show_url = result.get_show_url().text;
				search_res = re.search(r'hsjrzbs',show_url)
				if search_res != None:
					print 1
			except BaseException , e:
				logging.error(repr(e))
