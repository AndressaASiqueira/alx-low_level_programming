#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

#My function
def add_new_country(country, visits, cities):
  travel = { "country" : country,"cities_visited":cities, "total_visits" : visits,}
  travel_log.append(travel) 

add_new_country("Russia", 2, ["Moscou", "Saint Petersburg"])

print(travel_log)

#teacher function

def add_new_country(country_visited, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = country_visited
  new_country["total_visits"] = times_visited
  new_country["cities_visited"] = cities_visited
  travel_log.append(new_country)
