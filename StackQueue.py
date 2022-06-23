def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False

def Push(stk,item):
    stk.append(item)
    top=len(stk)-1

def pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        top=len(stk)-1
        return stk[top]
        
