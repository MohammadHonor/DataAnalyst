def digit_sum(s:str)->int :
      num : int = int(s)
      sum : int = 0

      while num > 0 :
            last:int = num % 10 
            sum += last
            num = int(num / 10)
      return sum