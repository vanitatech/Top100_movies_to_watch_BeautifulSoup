
from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
response.raise_for_status()

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]


# Save the movies to a text file
with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

print("Movies saved to movies.txt")






































#with open("website.html", "r") as file:
#          content = file.read()
#soup = BeautifulSoup(content, "html.parser")
#soup.find_all(name="p")
