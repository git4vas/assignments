import requests as r
search_result = {}
search_term = input("Please enter a search term:")
search_result = r.get(f"https://itunes.apple.com/search?term=\
    {search_term}&entity=album").json()

print("The search returned", search_result["resultCount"], "results.")
for entry in search_result["results"]:
    print(f"Artist: {entry['artistName']} - Album: {entry['collectionName']}\
         - Track Count: {entry['trackCount']}")