# WAP print this patten 1 4 7 10 13 15 using for loop

for y in range (1,14,3):
     print(y)

#wap  print this pattern 1 3 7 11 13 15 using for

for b in range (1,16,2):
  if b==9 or b==5:
      continue #skip the current iteration
     
else:
    print(b)