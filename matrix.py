import numpy as np 

class Matrixcalculator:
   @staticmethod
   def add_matrices(matrix1, matrix2):
      return np.add(matrix1, matrix2).tolist() 
   
   @staticmethod
   def subtract_matrices(matrix1, matrix2):
      return np.subtract(matrix1, matrix2).tolist()
   
   @staticmethod 
   def multiply_matrices(matrix1, matrix2):
      return np.matmul(matrix1, matrix2).tolist()
   
   @staticmethod 
   def print_matrix(matrix):
      for row in matrix:
         print(' '.join('{elem:4}' for elem in row))

def get_matrix_from_user():
   rows = int(input("Enter the number of rows:"))
   cols = int(input("Enter the number of columns:"))

   matrix = []
   print("Enter the elements of the {rows}x{cols} matrix:")
   for i in range(rows):
      row = list(map(float, input("Enter {cols} elements for row {i+1}, separated by spaces: ").split())) 
      if len(row) != cols:
         raise ValueError("Expected {cols} elements, but got {len(row)}")
      matrix.append(row)

   return matrix 

def main():
 calc = Matrixcalculator()

 while True:
    print("\nMatrix Calculator Menu:")
    print("1. Add matrices")
    print("2. Subtract matrices")
    print("3. Multiply matrices")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '4':
       print("Thank you for using the Matrix calculator. Goodbye!")
       break 
    
    if choice in ['1', '2', '3']:
       print("\nFor the first matrix:")
       matrix1 = get_matrix_from_user()
       print("\nFor the second matrix:")
       matrix2 = get_matrix_from_user()

       print("\nFirst Matrix:")
       calc.print_matrix(matrix1)
       print("\nSecond matrix:")
       calc.print_matrix(matrix2)

       try:
          if choice == '1':
             result = calc.add_matrices(matrix1, matrix2)
             print("\nResult of addition:") 
          elif choice == '2':
             result = calc.subtract_matrices(matrix1, matrix2)
             print("\nResult of subtraction:")
          elif choice == '3':
             result = calc.multply_matrices(matrix1, matrix2)
             print("\nResult of multiplication:")

          calc.print_matrix(result)
       except ValueError as e:
          print("Error: {e}")
          print("Make sure the matrices have compatible dimensions for the chosen operation.")
    else:
       print("invalid choice. Please enter a nmber between 1 and 4.")