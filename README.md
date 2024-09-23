# Interview Challenge at Nilo Saúde Entries Validation

Consider a denormalized database structure that stores location in the form `city | state | country`.

Create a function that validates the integrity, assuring <mark>a city belongs to a single state</mark>, <mark>and</mark> <mark>a state belongs to a single country</mark>.

````
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
````
