#select_course

import urllib.request
import urllib.parse
import urllib.response
import http.cookiejar
import http.cookies
import re
import io
import sys
from get_user_info import classid
from Login import login

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')
select_url = 'http://jwfw.fudan.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=141'

def select_course():
	req = urllib.request.Request(select_url)
	response = urllib.request.urlopen(req)
	data = response.read().decode('utf-8')
	print(data)
