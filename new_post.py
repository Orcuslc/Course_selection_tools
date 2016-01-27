#rewrote the post module with requests
import requests
import re
from get_user_info import courseid
from new_login import login_client

class post_client(login_client):
	def __init__(self):
		super().__init__()
		super().login()
		self._course_id = self._course_data[courseid][0]
		self._post_status = False
		self._select_status = False

	def _select(self):
		post_url = 'http://xk.fudan.edu.cn/xk/stdElectCourse!batchOperator.action?profileid=141'
		post_values = {
			'optype':'true',
			'operator0':self._course_id.join(':true:0')
		}
		headers = {
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Accept': 'text/html, */*; q=0.01',
			'X-Requested-With': 'XMLHttpRequest',
			'Referer': 'http://xk.fudan.edu.cn/xk/stdElectCourse!defaultPage.action?electionProfile.id=141',
			'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3',
			# 'Accept-Encoding': 'gzip, deflate',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.11102',
			'Content-Length': 39,
			'DNT': 1,
			'Host': 'xk.fudan.edu.cn',
			'Connection': 'Keep-Alive',
			# 'Pragma': 'no-cache',
			# 'Cookie': 'JSESSIONID=F0167895F244CF43B6B43075FF47CA6F.62-; SVRNAME=xk1'
		}
		req = self._session.post(post_url, data = post_values, headers = headers)
		print(req.text)

	def select(self):
		if self._course_status == True:
			print('Data Complete')
		self._select()

if __name__ == '__main__':
	pclient = post_client()
	pclient.select()