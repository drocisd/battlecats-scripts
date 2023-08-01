import os
import shutil

def t3str(s):
	return str(s).rjust(3, '0')

for i in sorted(os.listdir('org/unit')):
	id = int(i)
	ids = t3str(id)
	shutil.copyfile('org/unit/' + ids + '/unit' + ids + '.csv', 'all/' + str(id))
