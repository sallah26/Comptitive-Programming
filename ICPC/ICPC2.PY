# \\\\\\\\\\\\\ QUADRANT DETERMINER
x=int(input())
y=int(input())
if(x>0):
    if(y>0):
        print("quadrant 1")
    else:
        print("quadrant 4")
if(x<0):
    if(y>0):
        print("quadrant 2")
    else:
        print("quadrant 3")