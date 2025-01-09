def updateQuantityInventory(stock, quantity):
    if(quantity>0):
        stock = stock + quantity
        return stock
    else:
        return stock