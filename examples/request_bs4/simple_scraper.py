import requests #importing the requests library to handle HTTP requests
from bs4 import BeautifulSoup #importing BeautifulSoup from the bs4 library to parse HTML content

url = "https://quotes.toscrape.com/"#URL of the webpage to scrape
response = requests.get(url)#sending a GET request to the specified URL

if response.status_code == 200:#checking if the request was successful
    soup = BeautifulSoup(response.text, 'html.parser') #parsing the HTML content of the webpage
    quotes = soup.find_all('span', class_='text') #finding all quote texts
    authors = soup.find_all('small', class_='author') #finding all authors    

    for q, a in zip(quotes, authors):   #iterating through quotes and authors simultaneously
        print(f"{q.text} — {a.text}")       #printing each quote along with its author      
else:                   #handling the case where the request was not successful             
    print("Failed to retrieve the webpage.")    #printing an error message
