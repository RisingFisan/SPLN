import requests
from bs4 import BeautifulSoup
import time

movies = {
    'Star Wars: The Phantom Menace (Episode I)': "https://imsdb.com/scripts/Star-Wars-The-Phantom-Menace.html",
    'Star Wars: Attack of the Clones (Episode II)': "https://imsdb.com/scripts/Star-Wars-Attack-of-the-Clones.html",
    'Star Wars: Revenge of the Sith (Episode III)': "https://imsdb.com/scripts/Star-Wars-Revenge-of-the-Sith.html",
    'Star Wars: A New Hope (Episode IV)': "https://imsdb.com/scripts/Star-Wars-A-New-Hope.html",
    'Star Wars: The Empire Strikes Back (Episode V)': "https://imsdb.com/scripts/Star-Wars-The-Empire-Strikes-Back.html",
    'Star Wars: Return of the Jedi (Episode VI)': "https://imsdb.com/scripts/Star-Wars-Return-of-the-Jedi.html",
    'Star Wars: The Force Awakens (Episode VII)': "https://imsdb.com/scripts/Star-Wars-The-Force-Awakens.html",
}

for movie, url in movies.items():
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        content = soup.find('td', class_="scrtext").findChild("pre").text
    except AttributeError:
        content = soup.find('td', class_="scrtext").text

    with open('_'.join(movie.lower().replace(':','').split()) + '.txt', 'w') as f:
        f.write(content)

    time.sleep(1)

