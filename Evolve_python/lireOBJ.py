import pickle
print('nom du fichier sans le obj')
dos=input()
source = open(dos+'.obj')
lines = source.readlines()



f = open(dos, "wb")


for i in range(0,len(lines)):
	if lines[i][0]=='f':
		a=lines[i].split()
		z=[]
		for j in a:
			
			if j!='f':
				b=j.split('//')
				
				for i in range(0,len(b)):
					b[i]=int(b[i])
				z.append(b)
		
		pickle.dump(z,f)
			
pickle.dump('fin',f)			

c=0
print(lines)
for i in range(0,len(lines)):
	if lines[i].split()[0]=='v':
		a=lines[i].split()
		for j in range(0,len(a)):
			if a[j]!='v':
				a[j]=float(a[j])
		
		pickle.dump(a,f)
		c=c+1
pickle.dump('fin',f)	
print(c)
c=0
for i in range(0,len(lines)):
	if lines[i].split()[0]=='vn':
		a=lines[i].split()
		for j in range(0,len(a)):
			if a[j]!='vn':
				a[j]=float(a[j])
		c=c+1
		
		pickle.dump(a,f)
pickle.dump('fin',f)
print(c)

for i in range(0,len(lines)):
	if lines[i].split()[0]=='vt':
		a=lines[i].split()
		for j in range(0,len(a)):
			if a[j]!='vt':
				a[j]=float(a[j])
		pickle.dump(a,f)
pickle.dump('fin',f)
f.close()
