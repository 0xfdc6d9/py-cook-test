import re
import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
response = requests.get("https://10.0.62.21/source/videoPlay", verify=False)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all 'a' tags
links = soup.find_all("a")

# Extract the href attribute of each link
urls = [link.get("href") for link in links]

file_sizes = re.findall(r'\d+[G|M|K]', str(response.content))

print(urls)
print(file_sizes)
