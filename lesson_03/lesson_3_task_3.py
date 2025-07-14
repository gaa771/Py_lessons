from address import Address
from mailing import Mailing

to_address = Address("112233", "Казань", "Профсоюзная", "1", "10")
from_address = Address("443355", "Рязань", "Октябрьская", "15", "5")

mailing = Mailing(to_address, from_address, 4500, "AB123456789RU")

print(f"Отправление {mailing.track} из {mailing.from_address.index} "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city} "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
