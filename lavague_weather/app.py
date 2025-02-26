import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import json

# In[];
# Load environment variables from .env file
load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_ENDPOINT = os.getenv("WEATHER_API_ENDPOINT")

# In[];
# Added LaVague base class implementation
class LaVague:
	"""
	Base class for agent implementations.
	"""

	def __init__(self):
		self.agent_name = self.__class__.__name__

	def get_agent_info(self):
		return f"Agent: {self.agent_name}"

# In[];
# Agent 1: News Summarizer
class NewsSummarizer(LaVague):
	def __init__(self, url="https://news.ycombinator.com/"):  # Changed default URL to Hacker News
		super().__init__()
		self.url = url
		self.news_summary = ""

	def fetch_and_summarize(self):
		try:
			# More comprehensive headers to appear like a legitimate browser
			headers = {
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Connection': 'keep-alive',
				'Upgrade-Insecure-Requests': '1',
				'Cache-Control': 'max-age=0'
			}

			response = requests.get(self.url, headers=headers)
			response.raise_for_status()

			soup = BeautifulSoup(response.content, 'html.parser')

			# Customize the parsing logic based on the website structure
			# For Hacker News
			if "news.ycombinator.com" in self.url:
				titles = soup.find_all('span', class_='titleline')
				summaries = [title.get_text() for title in titles][:5]  # Get top 5 news
				self.news_summary = " | ".join(summaries)
			# BBC News
			elif "bbc.com" in self.url or "bbc.co.uk" in self.url:
				article_elements = soup.find_all('h3', class_='gs-c-promo-heading__title')
				summaries = [element.get_text().strip() for element in article_elements][:5]
				self.news_summary = " | ".join(summaries)
			# CNN
			elif "cnn.com" in self.url:
				article_elements = soup.find_all('span', class_='container__headline-text')
				summaries = [element.get_text().strip() for element in article_elements][:5]
				self.news_summary = " | ".join(summaries)
			# Default fallback
			else:
				# Try a more generic approach
				headlines = soup.find_all(['h1', 'h2', 'h3'])[:5]  # Get first 5 headlines
				summaries = [h.get_text().strip() for h in headlines if len(h.get_text().strip()) > 15]
				self.news_summary = " | ".join(summaries) if summaries else "Could not find article content."

			return True
		except requests.exceptions.RequestException as e:
			print(f"Error fetching URL: {e}")
			self.news_summary = f"Error: {e}"
			return False
		except Exception as e:
			print(f"An unexpected error occurred: {e}")
			self.news_summary = f"An unexpected error occurred: {e}"
			return False

	def get_summary(self):
		self.fetch_and_summarize()
		return json.dumps({"summary": self.news_summary}, indent=4)

# In[];
# Agent 2: Weather Report Agent
class WeatherAgent(LaVague):
	def __init__(self, city):
		super().__init__()
		self.city = city
		self.weather_data = {}

	def fetch_weather(self):
		try:
			params = {
				"key": WEATHER_API_KEY,
				"q": self.city,
				"aqi": "no"
			}

			# Replace with a real weather API (e.g., OpenWeatherMap)
			response = requests.get(WEATHER_API_ENDPOINT, params=params)
			response.raise_for_status()
			self.weather_data = response.json()  # Assuming JSON response
			return True
		except requests.exceptions.RequestException as e:
			print(f"Error fetching weather data: {e}")
			self.weather_data = {"error": f"Error: {e}"}
			return False
		except json.JSONDecodeError as e:
			print(f"Error decoding JSON response: {e}")
			self.weather_data = {"error": f"Error decoding JSON response: {e}"}
			return False
		except Exception as e:
			print(f"An unexpected error occurred: {e}")
			self.weather_data = {"error": f"An unexpected error occurred: {e}"}
			return False

	def get_weather(self):
		self.fetch_weather()
		return json.dumps(self.weather_data, indent=4)

# In[];
# Use: python3 app.py
#
if __name__ == "__main__":
	news_agent = NewsSummarizer("https://news.ycombinator.com/")
	weather_agent = WeatherAgent("London")

	print(news_agent.get_summary())
	print(weather_agent.get_weather())