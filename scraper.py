import requests
from bs4 import BeautifulSoup


def get_link_page(site):
    try:
        res = requests.get(site)
        if res.status_code == 200:
            return res.text
        else:
            print(f"Can't the fetch data from {site}")
            return None
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return None

def web_scraper(site):
    html_content = get_link_page(site)
    if html_content is not None:
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Remove the unwanted tags
        for unwanted_tags in soup(["script", "style"]):
            unwanted_tags.extract()
        
        # Extrated the span and a tags data
        span_tags = soup.find_all("span")
        a_tags = soup.find_all("a")
        
        span_text = [span.get_text(strip=True) for span in span_tags]
        a_text = [a.get_text(strip=True) for a in a_tags]
        
        scraped_data = '\n'.join(span_text + a_text)
        return scraped_data.strip()
    else:
        return None