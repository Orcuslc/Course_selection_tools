#main
from Login import login
from select import select_course

result = login()
print(result)

if result == False:
	raise BaseException('Server Error: Login Failed, Please try again')

select_course()			