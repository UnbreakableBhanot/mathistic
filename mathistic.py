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
        try:
            self.A = []
            self.__creator(self.A)
            print("Matrices formed for {} ".format(self))
            self.__show_matrix(self.A)
        except ValueError:
            print("Please Enter correct Integer Value")

    def __show_matrix(self, other):
        for i in other:
            print(i)
    
    def __add__(self,other):
        try:
            temp = []
            for i in range(len(self.A)):
                temp.append([])
                for j in range(3):
                    temp[i].append(int(self.A[i][j]) + int(other.A[i][j]))
        
            return temp
    
        except IndexError:
            print("For addition Matrices should be of same size")

        except ValueError:
            print("Please Enter correct Integer value")

    def __sub__(self,other):
        try:
            temp = []
            for i in range(len(self.A)):
                temp.append([])
                for j in range(3):
                    temp[i].append(int(self.A[i][j]) - int(other.A[i][j]))

            return temp

        except IndexError:
            print("For Subtraction Matrices should be of same size")

        except ValueError:
            print("Please Insert correct integer value")
            

    def __mul__(self,other):
        try:
            temp = None
            if len(self.A[0]) == len(other.A) and len(self.A) == len(other.A[0]):
                temp = []
            
                for i in range(len(self.A)):
                    temp.append([])
                    temp_left_add = 0
                    temp_right_add = 0
                    for j in range(len(other.A[0])+1):
                        temp_left_add += (int(self.A[i][j])*int(other.A[j][0]))
                        temp_right_add += (int(self.A[i][j])*int(other.A[j][1]))

                    temp[i].append(temp_left_add)
                    temp[i].append(temp_right_add)
                    
            else:
                print("multiplication is not possible")
                
            return temp
        except ValueError:
            print("Please Enter correct Integer Value")
