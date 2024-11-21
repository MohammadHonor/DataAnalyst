def reverse_first_last_Name(f : str , l : str ) -> str :
      first = list(f)
      first.reverse()
      last = list(l)
      last.reverse()
      new_str=""
      for v  in first :
            new_str += v
      new_str +=" "
      for v in last :
            new_str+=v
      return new_str