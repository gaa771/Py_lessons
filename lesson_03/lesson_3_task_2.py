from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "IPhone 15", "112223344"),
    Smartphone("Samsung", "Galaxy S10", "223334455"),
    Smartphone("Xiaomi", "15", "334445566"),
    Smartphone("Realme", "C755", "445556677"),
    Smartphone("Huawei", "P30", "556667788"),
]

for phone in catalog:
    print(f"{phone.phonemark} - "
          f"{phone.phonemodel}. {phone.phonenumber}")
