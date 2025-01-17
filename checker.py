from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

# Configurations
webhook_url = "<YOUR_DISCORD_WEBHOOK_URL>"
page_url = "https://store.steampowered.com/sale/steamdeckrefurbished/"
product_titles = [
    "Steam Deck 512GB OLED - Valve Certified Refurbished",
    "Steam Deck 1TB OLED - Valve Certified Refurbished",
    # "Steam Deck 64 GB LCD - Valve Certified Refurbished",
    # "Steam Deck 256 GB LCD - Valve Certified Refurbished",
    # "Steam Deck 512 GB LCD - Valve Certified Refurbished",
]
debug = False  # Set to True to always send a notification with a screenshot

# Set up Selenium WebDriver options
options = Options()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
service = Service("/usr/bin/chromedriver")  # Update with the correct path to your ChromeDriver

# Start WebDriver
driver = webdriver.Chrome(service=service, options=options)
try:
    driver.get(page_url)

    # Wait for page to load dynamic content
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Extra wait to ensure all dynamic content is fully loaded
    time.sleep(3)

    # Set the window size to capture the full page
    driver.set_window_size(1920, 1500)
    
    product_found = False
    for title in product_titles:
        try:
            # Check if the product is available
            product_element = driver.find_element(By.XPATH, f"//*[contains(text(), '{title}')]")
            
            # Locate the "Add to Cart" button (adjusted for your HTML structure)
            add_to_cart_button = product_element.find_element(By.XPATH, "..//following-sibling::*//*[contains(@class, 'CartBtn')]//span[contains(text(), 'Add to Cart')]")
            
            # Check if the "Add to Cart" button is present
            if add_to_cart_button.is_displayed():
                product_found = True
                break
        except Exception as e:
            # If any exception occurs (e.g., product not found), continue checking other products
            continue

    # Take a full-page screenshot
    screenshot_path = "/tmp/steamdeck_stock_status.png"
    driver.save_screenshot(screenshot_path)

    # Send a notification if any of the products have an "Add to Cart" button visible
    if product_found or debug:
        print("One of the Steam Deck models is now in stock!")
        message = {
            "content": f"One of the Steam Deck models is now in stock! Check it out here: <{page_url}>",
        }
        files = {
            "file": ("screenshot.png", open(screenshot_path, "rb"))
        }
        response = requests.post(webhook_url, data=message, files=files)
    else:
        print("Neither Steam Deck model is in stock!\nNo need to notify.")

finally:
    driver.quit()
