import requests

def fetch_movies(api_key):
    movies = []
    page = 1
    while True:
        url = f'http://www.omdbapi.com/?apikey={api_key}&s=movie&page={page}'
        response = requests.get(url)
        data = response.json()
        
        print(f"Fetching page: {page}, URL: {url}")
        print(f"Response data: {data}")

        if 'Error' in data:
            break

        movies.extend(data['Search'])

        total_results = int(data['totalResults'])
        if page > total_results // 10 + 1:
            break
        page += 1
    return movies

def group_movies_by_year_and_actor(movies):
    grouped_data = {}
    for movie in movies:
        year = movie['Year']
        actors = movie['Actors'].split(', ') if 'Actors' in movie else []
        if year not in grouped_data:
            grouped_data[year] = {}
        for actor in actors:
            if actor not in grouped_data[year]:
                grouped_data[year][actor] = 0
            grouped_data[year][actor] += 1
    return grouped_data
