def hash(char):

  long = 0
  p = 200
  level = 2**len(char)
  for i in range(len(char)):
    long = long + ord(char[i])*(p**i)
  long = long % level
  return long

char = ['h','e','l','l','o','w','o','r','l','d']
print("вх: ",char)
print("вых: ",hash(char))