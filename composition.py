from scipy import special
import math
from itertools import combinations
#http://www.fq.math.ca/Scanned/14-5/abramson.pdf
def summation_term_c32(k,j,n,t,w):
	temp1 = math.pow(-1,j)*special.binom(k,j)
	nom = n-k*(t-1)+j*(t-w-1)-1
	denom = k-1 
	if nom < denom:
		return 0
	result = temp1*special.binom(nom,denom)
	return result

def summation_term_32(n,k,j,h,diff):
	result = math.pow(-1,j)*jsummation_32(n,k,j,h,diff)
	return result

def jsummation_32(n,k,j,h,diff):
	result = 0
	for item in combinations(diff,j):
		temp = 0
		for i in item:
			temp = temp + i
		if (n-h+k-j-1-temp)>=k-1:
			result = result + special.binom(n-h+k-j-1-temp, k-1)

	return result

def jsummation_b3(n,k,j,p):
	result = 0
	for item in combinations(p,j):
		temp = 0
		for i in item:
			temp = temp + i
		if (n-1-temp)>=k-1:
			result = result + special.binom(n-1-temp, k-1)
	return result

def summation_term_b3(n,k,j,p):
	result = math.pow(-1,j)*jsummation_b3(n,k,j,p)
	return result

def restricted_composition(n,k,h,p):
	result = 0
	#Formula C
	if isinstance(h,int)and isinstance(p,int) and p!=n and h!=1:
		for j in range(0,k+1):
			result = result + summation_term_c32(k,j,n,h,p)
	#Formula 3.2
	elif isintance(h,list) and isinstance(p,list):
		diff = [j-i for i,j in zip(h,p)]
		result = special.binom(n-sum(h)+k-1,k-1)
		for j in range(1,k+1):
			result = result + summation_term_32(n,k,j,sum(h),diff)
	#Formula A
	elif isinstance(h,list) and isinstance(p,int) and p==n:
		nom = 0
		for i in h:
			nom += i
		result = special.binom(n+k-1-nom,k-1)
	#Formula B
	elif isinstance(p,list) and h==1:
		result = special.binom(n-1,k-1)
		for j in range(1,k+1):
			result = result + summation_term_b3(n,k,j,p)
	#Formula D
	elif isinstance(h,int) and p==n:
		result = special.binom(n-k*(t-1)-1,k-1)

	#Formula E
	elif h==1 and isinstance(p,int):
		for j in range(0,k+1):
			result = math.pow(-1,j)*special.binom(k,j)*(n-j*p-1,k-1)

	print result


restricted_composition(20,3,[4,5,6],[10,10,12])

#restricted_composition(6,3,1,3)
