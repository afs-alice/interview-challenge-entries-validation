entries = [
    ["Rio Branco", "Acre", "Brasil"],
    ["Rio Branco", "Sao Paulo", "Brasil"], # invalid 
    ["Boa Vista", "Acre", "Brasil"],
    ["Maceio", "Alagoas", "Brasil"],
    ["Rio Branco", "Acre", "Brasil"], # valid
    ["Toronto", "Ontario", "Canada"],
    ["Campinas", "Acre", "Canada"],  # invalid
    ["Toronto", "Distrito Federal", "Canada"],  # invalid
]

aux_1 = {}
for entrie in entries:
    city, state, country=entrie
    if not aux_1.get(city) and not aux_1.get(country):
        aux_1[city] = state, country
    else:
        print("Entrie now allowed, already exists.")
    print(aux_1)
