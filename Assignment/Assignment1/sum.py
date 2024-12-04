
def sum()->int :
      s:int = 0
      num: int = int(input("Enter three digit Number between 100 to 999 "))
      while num >0 :
            s+= num %10
            num = int(num /10)
      return s