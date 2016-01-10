#get data from the JWFW system

import urllib.request
import urllib.parse
import urllib.request
import urllib.response
import re

from Login import login

def get_data():
	page = login()
	data = page.info
	course_data = re.findall(r"id:\d{6},no:'\w{4}\d{6}.\d\d'", data)
	course_dict = {}
	for data in course_data:
		course_id = re.findall(r'\d{6}', data)[0]
		course_no = re.findall(r'\w{4}\d{6}.\d\d', data)[0]
		course_dict[course_no] = course_id
	return course_dict

