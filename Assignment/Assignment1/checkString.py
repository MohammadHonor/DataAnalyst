def check_string(s:str)->str:
      user:str = input("Enter your string ")
      if user in s :
            return "Present"
      else :
            return "Not Present"