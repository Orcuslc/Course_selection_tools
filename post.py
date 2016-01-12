 # push_course
import urllib.parse
import urllib.request
import urllib.response
import urllib.error
import http.client
import io
import sys
import re
import threading
import requests
from login import login_client
from get_user_info import courseid

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')

# class HTTPRequest( object ):

# 	def __init__( self, host, url, headers={}, secure=False ):
# 		self.host = host
# 		self.url = url
# 		self.secure = secure
# 		self.headers = {}
# 		self.type = self.get_type()
# 		for key, value in headers.items():
# 			self.add_header(key, value)

# 	def has_header( self, name ):
# 		return name in self.headers

# 	def add_header( self, key, val ):
# 		self.headers[key.capitalize()] = val

# 	def add_unredirected_header(self, key, val):
# 		self.headers[key.capitalize()] = val

# 	def is_unverifiable( self ):
# 		return True

# 	def get_type( self ):
# 		return 'https' if self.secure else 'http'

# 	def get_full_url( self ):
# 		port_str = ""
# 		port = str(self.host[1])
# 		if self.secure:
# 			if port != 443:
# 				port_str = ":"+port
# 		else:
# 			if port != 80:
# 				port_str = ":"+port
# 		return self.get_type() + '://' + self.host[0] + port_str + self.url

# 	def get_header( self, header_name, default=None ):
# 		return self.headers.get( header_name, default )

# 	def get_host( self ):
# 		return self.host[0]

# 	get_origin_req_host = get_host

# 	def get_headers( self ):
# 		return self.headers

class post_client(login_client):
	def __init__(self):
		super().__init__()
		super().login()
		self.course_id = self.course_data[courseid]
		self.post_status = False
		self.select_ststus = False

	def _select(self):
		'''
		原因在于，由于urllib不支持keep-alive，故与服务器之间的连接自动断开。
		试图使用http.client解决问题。
		'''
		post_url = 'http://jwfw.fudan.edu.cn/eams/stdElectCourse!batchOperator.action?profileid=141'
		post_values = {
			'optype':'true',
			'operator0':self.course_id.join(':true:0')
		}
		post_data = urllib.parse.urlencode(post_values).encode(encoding = 'utf-8')
		headers = {
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Accept': 'text/html, */*; q=0.01',
			'X-Requested-With': 'XMLHttpRequest',
			'Referer': 'http://jwfw.fudan.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=141',
			'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3',
			# 'Accept-Encoding': 'gzip, deflate',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.11082',
			'Content-Length': '39',
			'Host': 'jwfw.fudan.edu.cn',
			'Connection': 'Keep-Alive',
			'Pragma': 'no-cache',
			# 'Cookie':'JSESSIONID=BCCB0F9D60491827F5B800A1E7049E5C.82-; amlbcookie=02; iPlanetDirectoryPro=AQIC5wM2LY4Sfcx1B39uh3RpUgBDj%2B%2BlU82jTfNmAjsLUCI%3D%40AAJTSQACMDI%3D%23'
				}
		# request = urllib.request.Request(url = post_url, headers = headers, data = post_data)
		# request = HTTPRequest('jwfw.fudan.edu.cn', post_url, headers)
		# self.opener.addheaders = request
		requests.post(post_url, headers = headers, data = post_data)
		
		# info = self.opener.open(request).read().decode('utf-8')
		self.post_status = True
		return info

	def post(self):
		info = self._select()
		result1 = re.findall(r'选课成功', info)
		result2 = re.findall(r'人数已满', info)
		if result1 != []:
			self.select_status = 'Succeed'
		elif result2 != []:
			self.select_status = 'No vancacy'
		else:
			self.select_status = False
		print(info)
		print(self.select_status)

if __name__ == '__main__':
	client = post_client()
	client.post()