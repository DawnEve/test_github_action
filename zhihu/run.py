import time
import random

num=random.randint(0,9)
flag=num>7
date=int( time.strftime("%d", time.localtime()) )

timsString=time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
print(timsString)


if (date % 2 == 0) and (flag):
	print(flag)
	fa = open(r"test.txt", "a")
	fa.write( str(time.time()) +":\t"+ timsString + "\n" )
	fa.close()
else:
	print("--")
