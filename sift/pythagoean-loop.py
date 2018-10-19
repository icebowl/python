def csquared(a, b):
    c = a*a + b*b
    return c

def main():
	for i in range(1,1001):
		a = i
		b = i
		c2 = csquared(a,b)
		print (a,b,c2)
	
main() 

#http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html
