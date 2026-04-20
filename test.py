import random
while True:
    user_country = input("Please write your country:")
    allowed_countries = ['Russia','Azerbaijan','USA']
    if user_country not in allowed_countries:
        break
    russia_population = random.randint(100000, 500000)
    azerbaijan_population = random.randint(10000, 100000)
    russia_city = {'country': 'Russia', 'City': 'Moscow', 'Population': russia_population}
    azerbaijan_city = { 'country': 'Azerbaijan', 'City': 'Baku', 'Population': azerbaijan_population}
    usa_city = { 'country': 'JEWISH', 'City': 'FULL OF JEWS', 'Population': 'JEWSSSS' }
    if user_country == 'Russia':
        print(russia_city.values())
    elif user_country == "Azerbaijan":
        print(azerbaijan_city.values())
    elif user_country == "USA":
        print(usa_city.values())

