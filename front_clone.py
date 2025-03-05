from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

def scrape_website(url, output_file="index.html"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Run in headless mode (no UI)
        page = browser.new_page()

        # Set user-agent to avoid bot detection
        page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        })

        page.goto(url, timeout=60000)  # Visit website, wait up to 60s
        page.wait_for_load_state("networkidle")  # Wait until everything loads

        html = page.content()  # Get full HTML source code
        soup = BeautifulSoup(html, "lxml")
        try:
            # Remove scripts and styles
            for tag in soup(["script"]):
                tag.decompose()
        except:
            pass

        with open(f'{output_file}.html', "w", encoding="utf-8") as file:
            file.write(soup.prettify())

        browser.close()
        print(f"✅ Page saved as {output_file}")

# Example usage:
'''
scrape_website("https://amazon.com", "amazon")

'''
