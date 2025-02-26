import requests
import os
from bs4 import BeautifulSoup
import json
from dotenv import load_dotenv
from flask import Flask, render_template, request

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_ENDPOINT = os.getenv("WEATHER_API_ENDPOINT", "https://api.weatherapi.com/v1/current.json")


# Base class for agent implementations
class LaVague:
	def __init__(self):
		self.agent_name = self.__class__.__name__

	def get_agent_info(self):
		return f"Agent: {self.agent_name}"


# Agent 1: News Summarizer
class NewsSummarizer(LaVague):
	def __init__(self, url="https://news.ycombinator.com/"):
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
		return {"summary": self.news_summary}


# Agent 2: Weather Report Agent
class WeatherAgent(LaVague):
	def __init__(self, city):
		super().__init__()
		self.city = city
		self.weather_data = {}

	def fetch_weather(self):
		if not WEATHER_API_KEY:
			print("Weather API key is not set")
			self.weather_data = {"error": "Weather API key is not configured"}
			return False

		try:
			params = {
				"key": WEATHER_API_KEY,
				"q": self.city,
				"aqi": "no"
			}

			response = requests.get(WEATHER_API_ENDPOINT, params=params)
			response.raise_for_status()
			self.weather_data = response.json()
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
		return self.weather_data


@app.route("/", methods=["GET", "POST"])
def index():
	news_url = ""
	city = ""
	news_summary = {}
	weather_data = {}

	if request.method == "POST":
		news_url = request.form.get("news_url", "")
		city = request.form.get("city", "")

		# Instantiate and run the agents only if data is provided
		if news_url:
			try:
				news_agent = NewsSummarizer(news_url)
				if news_agent.fetch_and_summarize():
					news_summary = news_agent.get_summary()
				else:
					news_summary = {"error": "Error processing news."}
			except Exception as e:
				news_summary = {"error": f"Error: {str(e)}"}

		if city:
			try:
				weather_agent = WeatherAgent(city)
				if weather_agent.fetch_weather():
					weather_data = weather_agent.get_weather()
				else:
					weather_data = {"error": "Error fetching weather."}
			except Exception as e:
				weather_data = {"error": f"Error: {str(e)}"}

	# Convert to JSON strings for template
	news_summary_json = json.dumps(news_summary, indent=4)
	weather_data_json = json.dumps(weather_data, indent=4)

	return render_template("index.html",
	                       news_summary=news_summary_json,
	                       weather_data=weather_data_json,
	                       news_url=news_url,
	                       city=city)

if __name__ == "__main__":
	app.run(debug=True)