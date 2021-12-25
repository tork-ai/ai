import os
import csv

files = [f for f in os.listdir('.') if os.path.isfile(f)]
c = 0
for f in files:
	if '.jpg' in f:
		c += 1
		if c == 6194:
			print(f)
			
print(c)


# print(c)

resultFile = open("list.csv", 'w', encoding="utf-8")

for r in files:
	if 'jpg' in r:
		resultFile.write( 'data/'+ r + ",")

	
resultFile.close()
##
##
##if __name__ == '__main__':
##	main()
