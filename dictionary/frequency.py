# Count frequency

def frequency_count(s:str)->dict:
      s_list:list[str] = list(s)

      # dict comprehension
      freq:dict[str,int] = {item : s_list.count(item) for item in set(s_list)}
      # freq:dict[int,int] = {item : s.count(item) for item in set(s)}
      return freq
