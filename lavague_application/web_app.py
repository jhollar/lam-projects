import lavague
import os

os.environ["LAVAGUE_TELEMETRY"] = "NONE"

# Import required modules
from lavague.core import WorldModel, ActionEngine, PythonEngine
from lavague.core.agents import WebAgent
from lavague.drivers.selenium import SeleniumDriver
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def main():
	# Initialize the Selenium driver, not in headless mode
	selenium_driver = SeleniumDriver(headless=False)

	# Initialize the WorldModel and ActionEngine
	world_model = WorldModel()
	action_engine = ActionEngine(selenium_driver)

	# Create a WebAgent with just world_model and action_engine
	# The error indicates python_engine should not be passed directly
	agent = WebAgent(
		world_model=world_model,
		action_engine=action_engine
	)

	# Initialize PythonEngine and add it to the agent after creation
	python_engine = PythonEngine(driver=selenium_driver)
	agent.python_engine = python_engine  # Set as an attribute if needed

	# Use the agent to navigate to a webpage
	agent.get("https://huggingface.co/docs")

	try:
		# Navigate to PEFT documentation
		agent.get("https://huggingface.co/docs/peft/index")

		# Look for quicktour specifically
		# Check if there's a "Quickstart" or "Get started" link and click it
		agent.run("Find and click on a link that says 'Quickstart', 'Quick Tour', or 'Get Started'")
	except Exception as e:
		print(f"Error: {e}")
		print("Trying alternative approach...")

		# Direct navigation to quicktour if known
		try:
			agent.get("https://huggingface.co/docs/peft/quicktour")
			print("Successfully navigated directly to PEFT quicktour")
		except Exception as e2:
			print(f"Second approach also failed: {e2}")


if __name__ == "__main__":
	main()