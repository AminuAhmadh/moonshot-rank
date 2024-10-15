import requests, os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

print("Starting...")

# App Store URL for the app to scrape
url = "https://apps.apple.com/us/app/moonshot/id6503993131"

# Telegram details
bot_token = os.getenv('BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')

# Function to send a message to Telegram
def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(telegram_url, data=data)

# Function to scrape the ranking
def scrape_ranking():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        ranking = soup.find('li', class_='product-header__list__item')

        if ranking:
            ranking_text = ranking.text.strip()
            return f"App Ranking: {ranking_text}"
        else:
            return "Ranking not found."
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Main function to scrape and send ranking
def main():
    ranking_info = scrape_ranking()
    send_telegram_message(ranking_info)

if __name__ == "__main__":
    main()
    print('sent message successful')
