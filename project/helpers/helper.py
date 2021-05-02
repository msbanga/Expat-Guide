import json as JSON
import os


# TODO : remove hardcoding
def update_data(country_data, happiness_factor, crime_freedom_factor):
    country_list = country_data.get('countries')
    total_countries = 190

    for data in country_list:
        crime_free_score = (50 - (data.get('crime_rate_rank') / total_countries) * 50) * crime_freedom_factor
        happiness_index_score = (50 - (data.get('happiness_index_rank') / total_countries) * 50) * happiness_factor
        score = happiness_index_score + crime_free_score
        data["score"] = score

    country_list.sort(key=lambda json: json['score'], reverse=True)
    return country_list


class Helper(object):

    # TODO : remove hardcoding
    def perform_operation(self, request_json):
        annual_salary = request_json.get('annualSalary')
        happiness_factor = int(request_json.get('happinessQuotient')) / 10
        tax_factor = int(request_json.get('taxStructure')) / 10
        job_market_factor = int(request_json.get('racialInclusivity')) / 10
        crime_freedom_factor = int(request_json.get('crimeFree')) / 10

        fn = os.path.join(os.path.dirname(__file__), 'Database.json')
        with open(fn) as f:
            country_data = JSON.load(f)

        country_list = update_data(country_data, happiness_factor, crime_freedom_factor)
        return JSON.dumps(country_list)

    def get_countries(self):
        fn = os.path.join(os.path.dirname(__file__), 'Database.json')
        with open(fn) as f:
            country_data = JSON.load(f)
        country_list = country_data.get('countries')
        name_list = [item.get('name') for item in country_list]
        return JSON.dumps(name_list)
