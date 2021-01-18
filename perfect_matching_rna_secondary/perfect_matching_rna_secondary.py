import sys
import math

def factorial(x):
	if (x==1):
		return x
	return x*factorial(x-1)

s = "AUACUUUUUGAUGGGUAUGGUGAACCUUCGGAAAGCCCUUCGACCCCACAAACUAAUUAAUGGUUAGGGCCA"
As = 0
Gs = 0 #assuming that the number of As == Us and Cs == Gs
for i in s:
	if i == 'A':
		As +=1
	if i == 'G':
		Gs +=1

print(factorial(As) * factorial(Gs))



