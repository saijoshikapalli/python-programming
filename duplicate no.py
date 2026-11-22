x=[1,2,3,4,2,4,5]
duplicate=[]
for i in x
  if x.count(i)>1 and i not in duplicate:
    duplicate.append(i)
  print(duplicate)
