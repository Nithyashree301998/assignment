class Food:
    def __init__(self,food_id,name,quantity,price,stock,discount):
        self.food_id=food_id
        self.name=name
        self.quantity=quantity
        self.price=price
        self.stock=stock
        self.discount=discount
    

    def set_food_id(self):
        self.food_id = food_id   

    
    def get_food_id(self):
        return self.food_id     

    
    def get_name(self):
        return self.name

    def set_name(self):
        self.name=name       

    
    def get_quantity(self):
        return self.quantity

    def set_quantity(self):
        self.quantity=quantity

    
    def get_price(self):
        return self.price

    def set_price(self):
        self.price=price       

    
    def get_stock(self):
        return self.stock

    def set_stock(self):
        self.stock=stock

    
    def get_discount(self):
        return self.discount

    def set_discount(self):
        self.discount=discount   


    def __str__(self):
        return f"Food_ID={self.food_id} \nName={self.name} \nQuantity={self.quantity} \nStock={self.stock} \nDiscoun{self.discount}"
                   