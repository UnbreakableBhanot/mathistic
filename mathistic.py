# Mathistic (currently in developing stage)
# It is a library made for automating the mathematical operations in your code
# Its current goal is to help developers to not to rewrite code for basic mathematical operations

# Author - Shubham Bhanot
# Version - 1
# First release - 24 jan 2024

class matrical:
    
    def __creator(self, Matrix):
        Rows = int(input("Enter number of Rows"))
        print("use space for next number","press enter for next line",sep="\n")
        for i in range(1,Rows+1):
            user_input = input("->")
            Matrix.append(user_input.split())

    def __init__(self):
        self.A = []
        self.__creator(self.A)
        print("Matrices formed for {} ".format(self))
        self.__show_matrix(self.A)
    
    def __show_matrix(self, other):
        for i in other:
            print(i)
    
    def __add__(self,other):
        temp = []
        for i in range(len(self.A)):
            temp.append([])
            for j in range(3):
                temp[i].append(int(self.A[i][j]) + int(other.A[i][j]))
        
        return temp