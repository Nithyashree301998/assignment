
from Final_project_admin import Admin
from Final_projectuser import User

class Main:
    def executeAdmin(self,choice):
        if choice==1:
            print("****Add fooditem***")
            admin.addFoodItem()
        if choice==2:
            print("****Edit fooditem***")
            admin.edit_food_item()
        if choice==3:
            print("****View fooditem***")
            admin.view_foodlist()
        if choice==4:
            print("****Remove fooditem***")  
            admin.remove_fooditem() 
        if choice==5:
            print("****Out of Admin page**** ")
            

    def executeUser(self,option):
    
        if option==1:    
            print("****Place new order****")    
            user.place_new_order()   
        if option==2:    
            print("****Order history****")    
            user.order_history()
        if option==3:    
            print("****Update profile****")    
            user.update_profile()            

    


   

main=Main()
admin=Admin()




while True:
    choice = int(input("Enter 1.Add food item \n2.Edit food item \n3.View the food list \n4.Remove the food item \n5.Out of Admin page:"))
    main.executeAdmin(choice)  
    if choice==5:
        break
    




user=User()
print("Enter the details for registration:")
user.registration()
print("Login to the Application-")
user.login()    
    
while True:
    option=int(input("Enter 1.Place order \n2.Order history \n3.Update profile:"))
    main.executeUser(option)




