import datetime

ar1 = ['banana','pear','apple']

print('Voorbeeld van een list')

for x in ar1:
	print(x)

print('Voorbeeld van een gedeeltelijke list')

for x in ar1[2:]:
	print(x)	

print('Voorbeeld van een tuple')
t1 = ('apple','banana','pear')
print(type(t1))
for x in t1:
  print(x)

print('Voorbeeld van een set')
s1 = {1,2,3}  
print(type(s1))
for x in s1:
	print(x)


print('Voorbeeld van een dictionary')
d1 =	{
  "voedsel": "twix",
  "cal": "255"
}

print(d1)  

print(d1.get('voedsel'))
print(d1['voedsel'])

tod = ( {'auto':'astonmartin', 'sportauto':'porsche'},{'groente':'tomaat', 'supergroente':'broccoli'})


print('key en value 1')
for x in tod:
	for y,z in x.items():
		print(y+','+z, end='')


for x in tod:
	print(x.values())		

print(dir(datetime))

'''
print('key en value 2')
for x,y in tod.items():
	print(x+','+y)
'''	