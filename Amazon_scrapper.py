import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://www.amazon.in/s?k=HP+15+13th+Gen+i5-1335U+Laptop"

# Add headers to avoid request blocking
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Send request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Find all products in the result page
results = soup.find_all("div", {"data-component-type": "s-search-result"})

print("="*80)
print("Scraped Products from Amazon")
print("="*80)

# Loop through each result and extract details
for item in results:
    # ASIN
    asin = item.get("data-asin", "N/A")

    # Title
    title = item.h2.text.strip() if item.h2 else "N/A"

    # Image URL
    image_tag = item.find("img", class_="s-image")
    image = image_tag["src"] if image_tag else "N/A"

    # Price
    price_whole = item.find("span", class_="a-price-whole")
    price_fraction = item.find("span", class_="a-price-fraction")
    if price_whole and price_fraction:
        price = f"₹{price_whole.text.strip()}{price_fraction.text.strip()}"
    else:
        price = "N/A"

    # Rating
    rating = item.find("span", class_="a-icon-alt")
    rating_text = rating.text.strip() if rating else "N/A"

    # Print product details
    print(f"\nASIN: {asin}")
    print(f"Title: {title}")
    print(f"Image URL: {image}")
    print(f"Price: {price}")
    print(f"Rating: {rating_text}")
    print("-" * 80)
