import re
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

# Retrieve the website content
response = requests.get("https://hi10anime.com")
html = response.text

# Parse the HTML content
soup = BeautifulSoup(html, "html.parser")

# Extract the page title
page_titles = soup.select("h1.widget-title")

if len(page_titles) > 1:
     second_title = page_titles[1]
     print(second_title.text.strip())
     print()

# Print the anime titles and number of views
# Access the attribute or method of each element in the list
titles = soup.select("a.wpp-post-title")
views = soup.select("span.wpp-views")

# Zip the lists together and collect the data in a list
data = []
for title, view in zip(titles, views):
     title_text = title.text.strip()
     view_text = view.text.strip()
     
     # Use a regular expression to match the brackets and their contents
     pattern = r"\[.*\]"
     # Replace the brackets and their contents with an empty string
     title_text = re.sub(pattern, "", title_text)
     
     data.append([title_text, view_text])

# Convert the data to tabular form and print it
print(tabulate(data, tablefmt="plain"))
print()

# Extract from the select category
select_element = soup.select_one("select#cat.postform")

# Extract the option elements inside the select element
options = select_element.find_all("option")

# Count the number of option elements
print(f"There are {len(options)} anime from the list")
