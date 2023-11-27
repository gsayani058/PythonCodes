a=5
def globalValueChange():
    global a
    a=10    
print("before call a=",a)#5
globalValueChange()#10
print("after call a=:",a)