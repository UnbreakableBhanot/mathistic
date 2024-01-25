# Matrical.py is sub class or library that can be used only for matrix purpose
# It helps devloper in addition for now in matrix upto fixed range extend

# Author - Shubham Bhanot
# Version - 1
# First release - 24 jan 2024

class matrical:
    
    def __creator(self, matrix):
        rows = int(input("Enter number of Rows: "))
        print("Use space for next number, press enter for next line",sep="\n")
        for i in range(rows):
            user_input = input("-> ")
            matrix.append(user_input.split())

    def __init__(self):
        try:
            self.A = []
            self.__creator(self.A)
            print("Matrix formed for {}".format(self))
            self.__show_matrix(self.A)
        except ValueError:
            print("Please enter correct integer values.")

    def __show_matrix(self, other):
        for row in other:
            print(row)

    def __add__(self, other):
        try:
            temp = []
            for i in range(len(self.A)):
                temp.append([])
                for j in range(3):
                    temp[i].append(int(self.A[i][j]) + int(other.A[i][j]))

            return temp

        except IndexError:
            print("For addition, matrices should be of the same size.")
        except ValueError:
            print("Please enter correct integer values.")

    def __sub__(self, other):
        try:
            temp = []
            for i in range(len(self.A)):
                temp.append([])
                for j in range(3):
                    temp[i].append(int(self.A[i][j]) - int(other.A[i][j]))

            return temp

        except IndexError:
            print("For subtraction, matrices should be of the same size.")
        except ValueError:
            print("Please enter correct integer values.")

    def __mul__(self, other):
        try:
            temp = None
            if len(self.A[0]) == len(other.A) and len(self.A) == len(other.A[0]):
                temp = []
                for i in range(len(self.A)):
                    temp.append([])
                    temp_left_add = 0
                    temp_right_add = 0
                    for j in range(len(other.A[0])):
                        temp_left_add += (int(self.A[i][j]) * int(other.A[j][0]))
                        temp_right_add += (int(self.A[i][j]) * int(other.A[j][1]))

                    temp[i].append(temp_left_add)
                    temp[i].append(temp_right_add)

            else:
                print("Multiplication is not possible")
                
            return temp
        except ValueError:
            print("Please enter correct integer values.")

    def transpose(self):
        temp = []
        for i in range(len(self.A[0])):
            temp.append([])
            for j in range(len(self.A)):
                temp[i].append(self.A[j][i])

        return self.__show_matrix(temp)

    
