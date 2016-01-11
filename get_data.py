#get data from the JWFW system

import urllib.request
import urllib.parse
import urllib.request
import urllib.response
import re
import json
from Login import login

def get_data():
	save_position = '\\data.json'
	page = login()
	page.login_status()
	if page.status == True:
		course_data_url = 'http://jwfw.fudan.edu.cn/eams/stdElectCourse!data.action?profileId=141'
		course_data_json = urllib.request.urlretrieve(course_data_url, save_position)

	# course_data = json.JSONDecoder(course_data_json)
	# data = page.info
	# course_data = re.findall(r"id:\d{6},no:'\w{4}\d{6}.\d\d'", data)
	# course_dict = {}
	# for data in course_data:
	# 	course_id = re.findall(r'\d{6}', data)[0]
	# 	course_no = re.findall(r'\w{4}\d{6}.\d\d', data)[0]
	# 	course_dict[course_no] = course_id
	# return course_dict
		return 1
	else:
		return 0

if __name__ == '__main__':
	course_dict = get_data()
	print(course_dict)
