from scipy import special
import math
#http://www.fq.math.ca/Scanned/14-5/abramson.pdf
def summation_term_c32(k,j,n,t,w):
	temp1 = math.pow(-1,j)*special.binom(k,j)
	nom = n-k*(t-1)+j*(t-w-1)-1
	denom = k-1 
	if nom < denom:
		return 0
	result = temp1*special.binom(nom,denom)
	return result
def restricted_composition(n,k,h,p):
	result = 0
	if isinstance(h,int)and isinstance(p,int):
		for j in range(0,k+1):
			result = result + summation_term_c32(k,j,n,h,p)
	print result


restricted_composition(6,3,1,3)
