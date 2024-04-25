#Lucky number#
a = b = c = d = (0,1,2,3,4,5,6,7,8,9)
for i in a:
  for j in b:
    for k in c:
      for l in d:
        luck = a[i]+b[j]+c[k]+d[l]
        if luck%9 == 0:
          print(a[i],b[j],c[k],d[l])
