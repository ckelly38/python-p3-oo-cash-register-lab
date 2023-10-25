#!/usr/bin/env python3

class CashRegister:
  def __init__(self, dc = 0):
    self.setDiscount(dc);
    self.total = 0;
    self.items = [];
    self.setNumItemsInLastTransaction(0);
    self.setLastTransaction(0);
  
  def getDiscount(self): return self._discount;

  def setDiscount(self, val):
    if (type(val) == int or type(val) == float): self._discount = val;
    else: print("discount must be a number.");
  
  discount = property(getDiscount, setDiscount);

  def getNumItemsInLastTransaction(self): return self._numitemsinlasttransaction;

  def setNumItemsInLastTransaction(self, val):
    if (type(val) == int and (0 < val or val == 0)): self._numitemsinlasttransaction = val;
    else: print("numitemsinlasttransaction must be a number.");
  
  numitemsinlasttransaction = property(getNumItemsInLastTransaction, setNumItemsInLastTransaction);

  def getLastTransaction(self): return self._last_transaction;

  def setLastTransaction(self, val):
    if (type(val) == int or type(val) == float): self._last_transaction = val;
    else: print("last_transaction must be a number.");
  
  last_transaction = property(getLastTransaction, setLastTransaction);
  
  def add_item(self, name, price, amount = 1):
    if (type(name) == str and (type(price) == int or type(price) == float) and type(amount) == int):
      for n in range(amount):
        self.items.append(name);
        self.total += price;
      self.numitemsinlasttransaction = amount;
      self.last_transaction = price;
    else: print("invalid item type found and used here!");
  
  def void_last_transaction(self):
    if (len(self.items) > 0):
      for n in range(self.getNumItemsInLastTransaction()):
        self.items.remove(self.items[len(self.items) - (n + 1)]);
        self.total -= self.last_transaction;
      self.setNumItemsInLastTransaction(0);
      self.setLastTransaction(0);
    return self.total;

  def apply_discount(self):
    if (self.getDiscount() < 0.01): print("There is no discount to apply.");
    else:
      self.total -= self.getLastTransaction() * self.getDiscount() / 100;
      print(f"After the discount, the total comes to ${int(self.total)}.");
      return None;

