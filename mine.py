#customer detatils
name = input("please input name")
e_mail = input("please input e-mail")
phone_number = int(input("please input number"))
tourist = ["name", "e-mail",phone_number]

#destination details
print("these are our destinations: mombasa, nairobi, kisumu, please type in one")
destination_name = ["mombasa","nairobi", "kisumu"]
departure_name = ["mombasa","nairobi", "kisumu"]
des_name = input()
if des_name in destination_name:
    print("thank you")
else:
    print("error")
print("these are our airport locations please select one for departure: mombasa, nairobi, kisumu, please type in one")
dep_name = input()
if dep_name in destination_name:
    print("thank you")
else:
    print("error")
description_place = ["beach","parks", "lake"]
location_place = ["mombasa","nairobi", "kisumu"]
print("these are our activities: beach, parks, lake")
des_place = input("please input an activity")
if des_place in description_place:
    print("thank you")
else:
    print("error")
tour_pack = des_name + "," + des_place
print("this is your tour pack", tour_pack)
if des_name == "mombasa":
    if dep_name == "nairobi":
        flight_price = 70
    elif dep_name == "kisumu":
            flight_price = 90
if des_name == "nairobi":
    if dep_name == "mombasa":
        flight_price = 70
    elif dep_name == "kisumu":
            flight_price = 80
if des_name == "kisumu":
    if dep_name == "nairobi":
        flight_price = 80
    elif dep_name == "mombasa":
            flight_price = 90
if des_place == "beach":
    activity_price = 50
elif des_place == "lake":
            activity_price = 40
elif des_place == "parks":
            activity_price = 80
print("this is your flight cost", flight_price)
print("this is your activity cost", activity_price)
total = activity_price + flight_price
print("and this is your total cost", total)
