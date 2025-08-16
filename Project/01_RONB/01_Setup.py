from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

# Setup
driver_path = "msedgedriver.exe"  # Adjust if needed
service = Service(driver_path)
driver = webdriver.Edge(service=service)

# Step 1: Open Facebook Page
driver.get("https://www.facebook.com/officialroutineofnepalbanda")

# Wait for manual login
input("Press Enter after logging in manually...")

# Step 2: Scroll the page to load posts
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print(f"Scrolled {i+1} times...")
    time.sleep(5)

# Step 3: Find and print post captions
post_divs = driver.find_elements(By.XPATH, "//div[@data-ad-comet-preview='message']")

print("\n📝 Post Captions:")
for i, post in enumerate(post_divs):
    print(f"\nPost {i+1}:")
    print(post.text)

# Close the browser after scraping
driver.quit()
