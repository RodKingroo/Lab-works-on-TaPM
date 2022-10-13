#Copyright (c) 2021 RodKingroo

def bitInput():
  
  bitString1 = input('������� bit string:')

  if len(bitString1)>8:
    print('������������ ����! ')
    exit()

  for b in bitString1:
    if b!='0' and b!='1':
      print('������������ ����!')
      exit()

  s1=8-len(bitString1)
  suffix = '0'*s1
  bitString1 = suffix + bitString1
  return bitString1

def filebitInput(filename):
  try:
    file = open(filename, 'r')
  except:
    print("���������� ������� ����")
    exit()

  bitString1 = file.readline()

  if len(bitString1)>8:
    print('������������ ����! ')
    exit()

  for b in bitString1:
    if b!='0' and b!='1':
      print('������������ ����!')
      exit()

  s1=8-len(bitString1)
  suffix = '0'*s1
  bitString1 = suffix + bitString1
  return bitString1
  
def conjaction(bitString1, bitString2):

  result = ''
  i=0
  while (i<8):
    if bitString1[i]== '1' and bitString2[i]== '1':
      result+='1'
    else:
      result+='0'
    i+=1
  return result

def filebitOutput(filename, bitString):
  try:
    file = open(filename, 'w')
  except:
    print("���������� ������� ����")
    exit()
  file.write(bitString)
  file.close()

a = filebitInput("a.txt")
print("bit string 1:", a)
b = bitInput()
print("bit string 2:", b)
c = conjaction(a, b)
filebitOutput("c.txt", c)
print('���������: ', c)
