class Order():
  def __init__(self, name, amount, email):
    self.name = name
    self.amount = amount
    self.email = email
  
  def __repr__(self):
    return f'Order n°{random.randint(1, 100)} referente a {self.name} para {self.email}'
