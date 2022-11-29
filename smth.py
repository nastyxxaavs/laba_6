x=7*729**6+6*81**9+3**14-90
mas=[0]*9
while x>0:
       mas[x%9]+=1
       x=x//9
print(mas)
