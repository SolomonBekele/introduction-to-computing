a=int(raw_input("enter side a: "))
b=int(raw_input("enter side b: "))
c=int(raw_input("enter side c: "))
if a+b>c and a+c>b and b+c>a:
    print "True"
else:
    print "False"
