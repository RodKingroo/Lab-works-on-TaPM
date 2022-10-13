#Copyright (c) 2021 RodKingroo

class BitString:

    def bitInput(self):
  
        self.bitString = input('������� bit string:')

        if len(self.bitString)>8:
        
            print('������������ ����! ')
        
            exit()

        for b in self.bitString:
        
            if b!='0' and b!='1':
        
                print('������������ ����!')
                exit()

        s1=8-len(self.bitString)
        suffix = '0'*s1
        self.bitString = suffix + self.bitString
        
    def filebitInput(self, filename):
        try:
            file = open(filename, 'r')
        except:
           
            print("���������� ������� ����")
            exit()

        self.bitString = file.readline()

        if len(self.bitString)>8:
           
            print('������������ ����! ')
            exit()

        for b in self.bitString:
           
            if b!='0' and b!='1':
           
                print('������������ ����!')
                exit()

        s1=8-len(self.bitString)
        suffix = '0'*s1
        self.bitString = suffix + self.bitString

    def output(self):
        print(self.bitString)
    
    def fileOutput(self, filename):
        try:
            file = open(filename, 'w')
        except:
            print("���������� ������� ����")
            exit()
        file.write(self.bitString)
        file.close()

    def conjaction(self, bS):

        result = ''
        i=0
        
        while (i<8):
            
            if self.bitString[i]== '1' and bS.bitString[i]== '1':
                result+='1'
            else:
                result+='0'

            i+=1
        
        return BitString(result)

    def __init__(self, init_str = None):
        
        if init_str != None:
        
            self.bitString = init_str
            
            if len (self.bitString)>8:
            
                print('������������ ����! ')
            
                exit()

            for b in self.bitString:
            
                if b!='0' and b!='1':
            
                    print('������������ ����!')
                    exit()

            s1=8-len(self.bitString)
            suffix = '0'*s1
            self.bitString = suffix + self.bitString




