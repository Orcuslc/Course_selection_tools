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

def login_selection_page():
	select_url = 'http://jwfw.fudan.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=141'
	cookiejar = http.cookiejar.CookieJar()
	cookie_support = urllib.request.HTTPCookieProcessor(cookiejar)
	opener = urllib.request.build_opener(cookie_support)
	headers = {
		# 'GET':'/eams/stdElectCourse!defaultPage.action?electionProfile.id=141 HTTP/1.1',
		'Accept':'text/html, application/xhtml+xml, image/jxr, */*',
		'Accept-Language':'zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3',
		'Referer':'http://jwfw.fudan.edu.cn/eams/stdElectCourse!innerIndex.action?projectId=1',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.11082',
		# Accept-Encoding: gzip, deflate
		'Host':'jwfw.fudan.edu.cn',
		'Connection':'Keep-Alive',
		'Cookie':'JSESSIONID=FBC559228A450593AC3DD9E3AD89E63C.82-; amlbcookie=01; iPlanetDirectoryPro=AQIC5wM2LY4Sfcx56KrhmUxxYAPHgu1vsyIkdTSWl5GFX7I%3D%40AAJTSQACMDE%3D%23'
		}

	for key in headers:
		opener.addheaders = [(key, headers[key])]

	op = opener.open(select_url)
	info = op.read().decode('utf-8')
	print(info)

if __name__ == '__main__':
	login_result = login()
	print(login_result)
	select_course()