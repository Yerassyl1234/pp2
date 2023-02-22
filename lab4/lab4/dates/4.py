from datetime import datetime
from datetime import time
date1=datetime.strptime('2020-12-12 12:12:12', '%Y-%m-%d %H:%M:%S')
today=datetime.now()
res=today-date1
print(res.days*24*3600+res.seconds)