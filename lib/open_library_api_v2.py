import requests
import json


class Search:

    def get_search_results_json(self):
        search_term = "the lord of the rings"

        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        print(URL)
        response = requests.get(URL)
        return response
    

#results = Search().get_search_results()
#print(results)