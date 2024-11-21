def swap()->None:
      """
      condition 
      first -> second
      second -> third 
      third -> first

      """
      first:int = int(input("Enter 1st Number "))
      second:int = int(input("Enter 2nd Number "))
      third:int = int(input("Enter 3rd Number "))
      
      print(f"Before swapping first Number is {first} second number is {second} third number is {third}")

      temp:int = second
      second = first 
      first = temp

      temp = third
      third = first
      first = temp

      print(f"After swapping first number is {first} second number is {second} third number is {third}")


