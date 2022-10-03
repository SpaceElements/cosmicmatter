import os
import shutil

original =r'C:\Windows\file.txt'
target = r'C:\Windows\1.txt'
x = 1
while x < 10000:
	pathx = x
	target = r'C:\Windows\\' + str(pathx) + r'.jpg'
	x += 1
	shutil.copyfile(original, target)

