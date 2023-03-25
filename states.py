import json

Dict = {
    "Karnataka" : "Bangalore",
    "TamilNadu" : "Chennai",
    "Kerala" : "Thiruvanathapuram",
    "AndhraPradesh" : "Amaravathi",
    "Telangana" : "Hyderabad",
    "Goa" : "Panaji",
    "Maharastra" : "Mumbai"

}

file = open("C:\\Users\\Vishnu\\vs code\\Assignment6_Q1a\\state_capital.json","w")
json.dump(Dict,file)
