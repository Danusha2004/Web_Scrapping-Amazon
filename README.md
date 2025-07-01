## Web_Scrapping
What is Web Scraping?
Web scraping is the process of extracting data from websites automatically using software or scripts. It's like a robot that reads websites for you and pulls out the information you're interested in — like prices, reviews, news articles, product listings, job postings, etc.

## Why is Web Scraping Used?
Some common use cases:

📈 Price comparison (e.g., Amazon, Flipkart)

📰 News aggregation

📊 Market research

💼 Job data extraction (e.g., LinkedIn, Indeed)

🧠 Training datasets for ML/AI

🧾 Monitoring website changes (stock levels, prices, new content)
---
## Amazon Product Scraper

This is a Python script that scrapes product information from Amazon India using `requests` and `BeautifulSoup`.

## 📌 Features
- Scrapes multiple pages from Amazon
- Extracts:
  - 📦 Product Title
  - 💵 Price
  - ⭐ Rating
  - 📝 Number of Reviews
  - 📦 Availability
- Saves to `products.csv` or `amazon_products.csv`
- Rotates user-agents to avoid detection
- Includes polite scraping delay to avoid blocking
- 
## ⚙️ Installation
pip install -r requirements.txt

### 🧰 Common Python Libraries

| Library         | Use                                 |
|-----------------|-------------------------------------|
| `requests`      | To fetch webpage HTML               |
| `BeautifulSoup` | To parse and navigate HTML          |
| `lxml`          | Fast HTML parser                    |
| `pandas`        | To store and save structured data   |
| `fake-useragent`| To rotate browser headers           |
| `selenium`      | For JavaScript-heavy websites       |

