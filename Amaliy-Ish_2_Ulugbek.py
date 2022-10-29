#A
x1 = int(input("x1="))
y1 = int(input("y1="))

#B
x2 = int(input("x2="))
y2 = int(input("y2="))

#S
x3 = int(input("x3="))
y3 = int(input("y3="))

AS = ((x3-x1)**2+(y3-y1)**2)**(0.5)
BS = ((x3-x2)**2+(y3-y2)**2)**(0.5)
ASBS = AS+BS
print(f"AS={AS}\nBS={BS}\nAS+BS={ASBS}\n")
