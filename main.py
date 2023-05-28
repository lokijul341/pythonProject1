a=[]
for i in range(20000100000,4*10**10,100000):
    if i % 3 == 0 and i % 100000 ==0 and i % 17 !=0 and i % 29 !=0 and i % 101 !=0 and i % 103 !=0:
        a.append(i)
print(len(a),min(a))
