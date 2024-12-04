def calculate_cost_price(selling_price:int , loss_percentage:int)->float:
      cost_price: float = (selling_price*100 )/(100 - loss_percentage)
      return cost_price