entries = [
    ["Rio Branco", "Acre", "Brasil"],
    ["Rio Branco", "Sao Paulo", "Brasil"],  # invalid
    ["Boa Vista", "Acre", "Brasil"],
    ["Maceio", "Alagoas", "Brasil"],
    ["Rio Branco", "Acre", "Brasil"],  # valid
    ["Toronto", "Ontario", "Canada"],
    ["Campinas", "Acre", "Canada"],  # invalid
    ["Toronto", "Distrito Federal", "Canada"],  # invalid
]

city_state_country = {}
state_country = {}

for entry in entries:
    city, state, country = entry

    # Check if the state is already registered with the same country
    if state in state_country and state_country[state] != country:
        print(f"Invalid entry (state-country mismatch): {entry}")
        continue  # Skip adding this entry

    # Check if the city is already registered with the same state and country
    if city in city_state_country:
        stored_state, stored_country = city_state_country[city]
        if stored_state != state or stored_country != country:
            print(f"Invalid entry: {entry}")
            continue  # Skip adding this entry

    # Add the city and state/country to the dictionary if valid
    city_state_country[city] = (state, country)
    state_country[state] = country

print(city_state_country)
