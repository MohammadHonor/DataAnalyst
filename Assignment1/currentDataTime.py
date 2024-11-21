from datetime import date
import time
def display_date_time() ->None :
      print(date.today())
      t=time.localtime()
      current_time = time.strftime("%H:%M:%S", t)
      print(current_time)