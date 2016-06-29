from string import Template
import os
filein=open('alert.txt')
src = Template( filein.read() )
lines = [line.rstrip('\n') for line in open('try.csv')]
os.system("kapacitor delete tasks alert_*")
for i in range(1,len(lines)):
	words = lines[i].split(",")
	measurement = words[0]

	fieldkey = words[1]
	warning =  words[2]
	critical = words[3]

	d = {'measurement':measurement, 'fieldkey':fieldkey , 'warning':warning , 'critical':critical }

	result = src.substitute(d)
	#print result
	f = open("file_"+str(i)+".tick","w")
	f.write(result)
	f.close()
	os.system("kapacitor define alert_"+str(i)+" -dbrp telegraf.default -tick file_"+str(i)+".tick -type stream")
	os.system("kapacitor enable alert_"+str(i))


	
