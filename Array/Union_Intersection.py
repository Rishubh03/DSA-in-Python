def Union(arrone, arrtwo):
  i=j=0

  while i<len(arrone) and j<len(arrtwo):
    if arrone[i] < arrtwo[j]:
      print(arrone[i])
      i += 1
    elif arrone[i] > arrtwo[j]:
      print(arrtwo[j])
      j += 1
    else:
      print(arrone[i])
      i += 1
      j += 1
  while i < len(arrone):
    print(arrone[i])
    i += 1
  while j< len(arrtwo):
    print(arrtwo[j])
    j += 1

def Intersection(arrone,arrtwo):
  i=j=0

  while i < len(arrone) and j < len(arrtwo):
    if arrone[i] < arrtwo[j]:
      i += 1
    elif arrone[i] > arrtwo[j]:
      j += 1
    else :
      print(arrone[i])
      i += 1
      j += 1

arrone = [1,3,5,7,9,11]
arrtwo = [2,4,6,8,10,11]
Union(arrone,arrtwo)
print("\n \n \n")
Intersection(arrone,arrtwo)
