'''
Enter side A: 11
Enter side B: 2
Enter side C: 4
Enter side D: 7
Enter side E: 1
'''
A = float(input("Enter side A: ")) 
B = float(input("Enter side B: "))
C = float(input("Enter side C: "))
D = float(input("Enter side D: "))
E = float(input("Enter side E: "))

rect1 = A * B
rect2 = (D - E - B) * (A - C)
tri = (A - C ) * E * 0.5

area = rect1 + rect2 + tri
print("Room Area: "+str(area))
        
