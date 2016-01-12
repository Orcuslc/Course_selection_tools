#main

from get_user_info import courseid, idnum, password
from post import post_client

def select_course():
	client = post_client()
	result = client.post()
	print(result)

if __name__ == '__main__':
	select_course()