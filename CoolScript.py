places = {
    "Apartment_A": {"type": "apartment", "cats": "zero_cats"},
    "House_B":     {"type": "house",     "cats": "many_cats_to_pet"}
}
preferences = {"type": "apartment", "cats": "many_cats_to_pet"}
priorities = ["type", "cats"]

for key, info_dict in places.items():
    x = 0
    for key1, value in info_dict.items():
        if key1 == "type":
            if value == preferences["type"]:
                x+=3
        if key1 == "cats":
            if value == preferences["cats"]:
                x+=2
    print(f"{key} {x}")