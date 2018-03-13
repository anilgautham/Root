dict = {2:'a',3:'b',5:'c',7:'d',9:'e',11:'f',13:'g',17:'h',19:'i'}
for i in range(1,26):
  print""
  count =0
  for key in sorted(dict):
    if(i%key==0):
      print dict[key],
      count+=1
  if(count==0):
    print i,