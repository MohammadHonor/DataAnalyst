def calculate_area(a:int , b: int , c: int) -> float :
      s : float = (a + b + c)/2
      return pow(s*(s-a)*(s-b)*(s-c) , 0.5)