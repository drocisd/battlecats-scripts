RWNAME = {}
RWSTNAME = {}
RWSVNAME = {}
for line in open('RewardName.txt'):
	s = line.rstrip().split('\t')
	if len(s) <= 1: continue
	name = s[1].rstrip()
	ids = s[0].rstrip().split('|')
	for i in ids:
		if i.startswith('S'):
			RWSTNAME[int(i.replace('S', ''))] = name
		elif i.startswith('I'):
			RWSVNAME[int(i.replace('I', ''))] = name
		else:
			RWNAME[int(i)] = name

def dump(obj, f):
	f.write('{')
	f.write(','.join('%s:"%s"' % (a, b) for a, b in obj.items()))
	f.write('}')

with open('RewardName.js', 'w') as f:
	f.write('const RWNAME=')
	dump(RWNAME, f)
	f.write(';\nconst RWSTNAME=')
	dump(RWSTNAME, f)
	f.write(';\nconst RWSVNAME=')
	dump(RWSVNAME, f)
	f.write(';\n')
