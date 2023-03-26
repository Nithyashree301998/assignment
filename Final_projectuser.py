from Final_project_admin import Admin


class User:

    def __init__(self,full_name=None,phone_num=None,email=None,address=None,password=None):
        self.full_name=full_name
        self.phone_num=phone_num
        self.email=email
        self.address=address
        self.password=password
        self.orders = []
        

    def set_full_name(self,full_name):
        self.full_name = full_name

    def get_full_name(self):
        return self.full_name       

    def set_phone_num(self,phone_num):
        self.phone_num=phone_num

    def get_phone_num(self):
        return self.phone_num     

    def set_email(self,email):
        self.email=email

    def get_email(self):
        return self.email  

    def set_address(self,address):
        self.address=address

    def get_address(self):
        return self.address       

    def set_password(self,password):
        self.email=password

    def get_password(self):
        return self.password 

    def __str__(self):
        return f"FullName={self.full_name},PhoneNumber={self.phone_num},Email={self.email},Address={self.address},Password={self.password}"


    def registration(self,full_name=None,phone_num=None,email=None,address=None,password=None):
        full_name=input("Enter the full name:")
        phone_num=input("Enter the phone number:")
        email=input("Enter the email:")
        address=input("Enter the full address:")
        password=input("Enter the password:")

    def login(self,email=None,password=None):
        email=str(input("Enter the email:"))
        password=str(input("Enter the password:"))
        user_obj= User(email,password)
        if email==user_obj.get_email():
            if password==user_obj.get_password():
                print("Login successfull")
        
        #else:
         #   print("Login unsuccessfull")


    order_items=[]       

    def place_new_order(self):
        food_items = Admin.food_items 
        print("List of all food items:")
        for food_item in food_items:
                print(f"{food_item.food_id}. {food_item.name} ({food_item.quantity}) [INR {food_item.price}] (Discount: {food_item.discount}%) (Stock: {food_item.stock})")
        selected_items = input("Enter the array of numbers for the items you want to order (separated by commas): ").split(",")
        selected_items = [int(x) for x in selected_items]
        order_items = [] 
        total_price = 0 
        for i in selected_items:
            if i <= len(food_items):
                food_item = food_items[i-1] 
                quantity = int(input(f"How many {food_item.name} do you want to order? "))
                if quantity > food_item.stock: 
                    print(f"Sorry, only {food_item.stock} {food_item.name} available")
                else:
                    order_items.append((food_item, quantity)) 
                    total_price += (food_item.price * quantity) 
                    food_item.stock -= quantity 
        if order_items: 
            print("Your order:")
            for item, quantity in order_items:
                print(f"{item.name} ({quantity}) [INR {item.price * quantity}]")
            print(f"Total price: INR {total_price}")
            confirm = input("Confirm your order (yes/no): ")
            if confirm.lower() == "yes":
                order = {"items": order_items, "total_price": total_price}
                self.orders.append(order) 
                print("Order confirmed")
            else:
                print("Order cancelled")
        else:
            print("No items selected for the order")        
    

    

    def order_history(self):
        if len(self.orders) > 0:
            for order in self.orders:
                print("Order Details:")
                for item, quantity in order["items"]:
                    print(f"{item.name} ({quantity}) [INR {item.price * quantity}]")
                print(f"Total price: INR {order['total_price']}")
                print("-------------")
        else:
            print("No orders found for this user")  


    def update_profile(self):
        full_name=input("Enter the full name:")
        phone_num=input("Enter the phonre number:")
        address=input("Enter the address:")
        password=input("Enter the password:")
        user_obj=User(full_name,phone_num,address,password)
        user_obj.set_full_name(full_name)
        user_obj.set_phone_num(phone_num)
        user_obj.set_address(address)
        user_obj.set_password(password)

        print("Profile successfully updated")
