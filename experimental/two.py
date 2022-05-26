import sys

for i in range(10):
    
    val = int(input())
    sys.stderr.write("From python(err) : "+str(val)+"\n")
    if val % 2 :
        print(1)
    else:
        print(0)
    
