from Final_project1 import Food


class Admin:

    food_items = []

    def addFoodItem(self):
        food_id = len(self.food_items)+1
        name=input("Enter the name of the food:")
        quantity=str(input("Enter the quantity:"))
        price=float(input("Enter the price of the item:"))
        stock=int(input("Enter the stock:"))
        discount=float(input("Enter the discount of the item:"))
        food_obj=Food(food_id,name,quantity,price,stock,discount)
        self.food_items.append(food_obj)
        print(f"Item added successfully with food_id:{food_id}")


    def edit_food_item(self,food_id=None,name=None,quantity=None,price=None,stock=None,discount=None):
        food_id=int(input("Enter the food id:"))
        for i in self.food_items:
            if food_id==i.get_food_id():
                name=input("Enter the name of the food:")
                quantity=int(input("Enter the quantity:"))
                price=float(input("Enter the price of the item:"))
                stock=int(input("Enter the stock:"))
                discount=float(input("Enter the discount of the item:"))     
        
                i.name(name)
                i.quantity(quantity)
                i.price(price)
                i.stock(stock)
                i.discount(discount)    

                print(f"food item with food id {food_id} is updated!")
                break  
            else:
                 print("Food item with food id{food_id} not found")


    def view_foodlist(self):
        print("List of all food items:")
        for food_item in self.food_items:
            print(f"Food id:{food_item.food_id},Name:{food_item.name},Quantity:{food_item.quantity},Price:[INR{food_item.price}],Discount:{food_item.discount}%,Stock:{food_item.stock}")


    def remove_fooditem(self,food_id=None):
        food_id=int(input("Enter the food id to be removed:"))
        for food_item in self.food_items:
            if food_id==food_item.get_food_id():
                self.food_items.remove(food_item)
                print("Food item removed successfully!")
                break
            else:
                print(f"No food item found with id {food_id}")

    
     