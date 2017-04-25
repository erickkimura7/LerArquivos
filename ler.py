#!/usr/bin/python3

import os
import glob


print(glob.glob('*.py'))

for each in glob.glob('*.py'):
	for line in open(each):
		print('#',line,end='')
	print()
	print()

print(os.system("locate .py > arq"))

with open('arq','r') as arq:
	for arquivo in arq:
		opa = arquivo.rsplit()
		with open(opa[0],'r') as txt:
			try:
				for line in txt:

					print (line)
			except:
				res = input("Error Continue ? [yes/no]")
				if res == 'yes':
					pass
				else:
					print("Saindo")
					break

			print('#############################################3')
