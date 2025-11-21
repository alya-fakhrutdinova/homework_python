from addess import Address
from mailing import Mailing



from_addr = Address("443109", "Самара", "Воеводина", "14", "50")
to_addr = Address("433511", "Димитровград", "Куйбышева", "259", "5")



mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=350,
    track="RU123456789RU"
)



print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.home} - {mailing.from_address.flat} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.home} - "
      f"{mailing.to_address.flat}. Стоимость {mailing.cost} рублей.")