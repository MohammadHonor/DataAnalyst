def create_new_string(s1 : str , s2 : str ) ->str :
      temp : str = s1[0:int(len(s1)/2) ]
      temp = temp + s2 + s1[int(len(s1)/2):int(len(s1))]

      return temp