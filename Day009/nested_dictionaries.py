import art
print(art.text2art("dict", font='block'), art.text2art("ion", font='block'),art.text2art("ary", font='block'))
#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
travel_log["France"] = {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits" : 12}
for k in travel_log:
    print(f"({k} --- {travel_log[k]}")
#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 13},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
for k in travel_log:
    print(f"({k} --- {travel_log[k]}")



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