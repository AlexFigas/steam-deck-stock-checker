# Steam Deck Refurbished Stock Checker

## Description

This project provides a script to monitor the availability of refurbished Steam Deck units on the official store page and send a notification to a specified Discord channel when stock is detected. The script uses Selenium for web scraping and a Discord webhook for notifications.

## Prerequisites

Before using this script, ensure the following dependencies are installed:

1. Python 3
2. Chromium or Google Chrome and ChromeDriver (compatible with your version of Chromium/Google Chrome). E.g for Ubuntu 24.04:
   ```sh
   sudo apt install chromium-browser chromium-chromedriver
   ```
3. Selenium and Requests Python packages (specified in requirements.txt)
   ```sh
   pip install -r requirements.txt
   ```

## Setup Instructions

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd steam-deck-stock-checker
   ```
2. Set up your Discord Webhook URL:
   - In checker.py, replace the placeholder webhook_url with your actual Discord webhook URL:
   ```python
   webhook_url = "YOUR_DISCORD_WEBHOOK_URL"
   ```
3. Set permissions and scheduling:
   - Ensure `script.sh` is executable:
   ```sh
   chmod +x script.sh
   ```
   - Add `script.sh` to a cron job to check for stock periodically (every 5 minutes in this example):
   ```sh
   */5 * * * * /bin/bash /path/to/steam-deck-stock-checker/script.sh
   ```

## Disclaimer

This script is provided "as is" for personal use. Be aware of website scraping policies and use responsibly.

## Alternative Setup with docker and docker compose

### Place your Discord URL

In checker.py, replace the placeholder webhook_url with your actual Discord webhook URL:

```python
webhook_url = "<YOUR_DISCORD_WEBHOOK_URL>"
```

### Select your desired steam decks to scrape

In checker.py, leave uncommented the steam decks you desire to scrape:

```python
product_titles = [
    "Steam Deck 512GB OLED - Valve Certified Refurbished",
    "Steam Deck 1TB OLED - Valve Certified Refurbished",
    # "Steam Deck 64 GB LCD - Valve Certified Refurbished",
    # "Steam Deck 256 GB LCD - Valve Certified Refurbished",
    # "Steam Deck 512 GB LCD - Valve Certified Refurbished",
]
```

### Start the Container

```sh
docker compose up --build -d
```

### Stop the Container

```sh
docker compose down
```

### Check Logs

```sh
docker exec -it sd-notifier cat /app/checker.log
```
