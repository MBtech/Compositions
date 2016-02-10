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
	result = math.pow(-1,j)*jsummation(n,k,j,h,diff)
	return result

def jsummation(n,k,j,h,diff):
	result = 0
	for item in combinations(diff,j):
		temp = 0
		for i in item:
			temp = temp + i
		if (n-h+k-j-1-temp)>=k-1:
			result = result + special.binom(n-h+k-j-1-temp, k-1)

	return result

def restricted_composition(n,k,h,p):
	result = 0
	if isinstance(h,int)and isinstance(p,int):
		for j in range(0,k+1):
			result = result + summation_term_c32(k,j,n,h,p)
	else:
		diff = [j-i for i,j in zip(h,p)]
		result = special.binom(n-sum(h)+k-1,k-1)
		for j in range(1,k+1):
			result = result + summation_term_32(n,k,j,sum(h),diff)
	print result


restricted_composition(20,3,[4,5,6],[10,10,12])

#restricted_composition(6,3,1,3)
