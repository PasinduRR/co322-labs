# E/19/310 - RANAGE R.D.P.R
# E/10/409 - UDAGAMASOORIYA D.P.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a//b

N = int(input())
eqns = []

for i in range(N):
    eqns.append([item for item in input().split()])
    # print(eqns)
    # for j in range(len(postfix_eqns) - 1):
    postfix_eqns = eqns[i]
    j = 0
    length = len(postfix_eqns)
    while(j < length - 1):
        # print('*')
        if(postfix_eqns[2] == '+'):
            # print('*')
            result = add(int(postfix_eqns[0]),int(postfix_eqns[1]))
            postfix_eqns.pop(0)
            postfix_eqns.pop(0)
            postfix_eqns.pop(0)
            postfix_eqns.insert(0, result)
            
        elif(postfix_eqns[2] == '-'):
            result = sub(int(postfix_eqns[0]),int(postfix_eqns[1]))
            postfix_eqns.pop(0)
            postfix_eqns.pop(0)
            postfix_eqns.pop(0)
            postfix_eqns.insert(0, result)
            
        elif(postfix_eqns[2] == '*'):
            result = mul(int(postfix_eqns[0]),int(postfix_eqns[1]))
            postfix_eqns.pop(0)
            postfix_eqns.pop(0)
            postfix_eqns.pop(0)
            postfix_eqns.insert(0, result)
            
        elif(postfix_eqns[2] == '/'):
            result = div(int(postfix_eqns[0]),int(postfix_eqns[1]))
            postfix_eqns.pop(0)
            postfix_eqns.pop(0)
            postfix_eqns.pop(0)
            postfix_eqns.insert(0, result)
            
        j+=2
    print(postfix_eqns[0])
        
        
    
