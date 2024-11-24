# dictionary of dictionary 
import json
def find_cub()->None:

      dic = {x : {"square":x**2,"cube":x**3} for x in range(1,5)}

      print(json.dumps(dic,indent=4))