list1 = ['c','o',['m',['p','u',['t','e'],'o'],'g'],'r','a','m']
list2 = ['r','p','r']
i = 0
for c in list2:
  list1[2][1][2].insert(2+i,c)
  i+=1
print(list1)