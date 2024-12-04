
def swap_with_two_sum ()->None :
      """
      condition
      1st= 1st + 2nd 
      2nd = 1st + 3rd
      3rd = 3rd + 2nd
      
      """
      print("Enter three Number in single line with space")
      ls:list[str] = input().split(" ")
      first:int = int(ls[0])
      second:int = int(ls[1])
      third:int = int(ls[2])
      print(f"Before condition apply \n First is {first} \n Second is {second} \n Third is {third}")
      temp: int = first
      first = first + second 
      temp2:int = second
      second = temp + third
      third = third + temp2
      print(f"After condition apply \n First is {first} \n Second is {second} \n Third is {third}")

