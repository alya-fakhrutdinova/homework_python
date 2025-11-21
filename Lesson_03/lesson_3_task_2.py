from smartphone import Smartphone


catalog = [
    Smartphone("IPhone", 15, "+79371767004"),
    Smartphone("Samsung", "S23", "+79279096565"),
    Smartphone("Nokia", 3310, "+79376306724"),
    Smartphone("POСО", "F7", "+79538712098"),
    Smartphone("HONOR", 400, "+79526384107")
]


for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.subscriber_number}")