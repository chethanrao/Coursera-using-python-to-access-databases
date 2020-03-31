
import re
file=open("/Users/chethanrao/Downloads/coursera/regexsum.txt")
sum=0
arraylist=list()
arraylist=file.readlines()
for line in arraylist:
	line=line.rstrip()
	nums=re.findall('([0-9]+)',line)
	for num in nums:
		sum=sum+int(num)
print(sum)

