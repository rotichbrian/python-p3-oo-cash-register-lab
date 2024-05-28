#!/usr/bin/env python3


class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  def add_item(self, item, price, quantity=1):
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(item)        
      self.previous_transactions.append({"item": item, "quantity": quantity, "price": price})    

  def apply_discount(self):
    if self.discount:
      self.total = int(self.total * ((100 - self.discount) / 100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if not self.previous_transactions:
      return "There are no transactions to void."
    self.total -= (
      self.previous_transactions[-1]["price"]
        * self.previous_transactions[-1]["quantity"]
        )
    for _ in range(self.previous_transactions[-1]["quantity"]):
      self.items.pop()
    self.previous_transactions.pop()

cash_register = CashRegister()
cash_register_with_discount = CashRegister(20)


cash_register_with_discount.add_item('macbook', 1000)
cash_register_with_discount.apply_discount()

cash_register.apply_discount()

new_register = CashRegister()
new_register.add_item("eggs", 1.99)
new_register.add_item("tomato", 1.76)
new_register.void_last_transaction()

print(new_register.total)
print(new_register.items)