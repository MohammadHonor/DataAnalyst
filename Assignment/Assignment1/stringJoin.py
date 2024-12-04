def string_join(s : str )->str :
      ls:list[str] = s.split(" ")
      modified_s : str = '-'.join(ls)
      return modified_s

