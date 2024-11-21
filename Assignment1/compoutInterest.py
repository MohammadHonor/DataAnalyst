def calculate_compound_interest()->None :
      ls:list[str] = input("Enter  Principal , Rate ,Time with single space in a line ").split(" ")
      
      P:int = int(ls[0])
      R:int = int(ls[1])
      T:int = int(ls[2])
      A:float = P*(pow((1+R/100),T))
      CI:float = A - P
      print(f"Compound Interest is {CI}")

