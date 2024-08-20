from bs4 import BeautifulSoup
import requests,openpyxl

try:
    # Send a GET request to the URL
    response = requests.get("https://aniwatch.to/search?keyword=top+animies")
    print("Api fetched: " + response);
    # Check if the request was successful (status code 200)
    
    soup = BeautifulSoup(response.text, "html.parser")
    #print(soup)
    genres=soup.find('ul',class_="ulclear color-list sb-genre-list sb-genre-less").find_all("li")
    #print(genres)

    workbook = openpyxl.Workbook()
    sheet = workbook.active

    sheet.append(["genres"])
    
    for genre in genres:
        genre_text = genre.text
        print(genre_text)

        sheet.append([genre_text])

        workbook.save("aniwatch-genre.xlsx")
except Exception as e:
    print("An error occurred:", e)
