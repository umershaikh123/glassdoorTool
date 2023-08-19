 import requests

class GlassdoorJobSearchingTool:
    def search_jobs(self, keywords, location):
        # Replace 'YOUR_API_KEY' with your actual Glassdoor API key
        api_key = 'YOUR_API_KEY'

        # Construct the API request URL with query parameters
        api_url = "https://api.glassdoor.com/api/api.htm"
        params = {
            "v": "1",  # API version
            "format": "json",  # Response format
            "t.p": api_key,  # Your API partner ID
            "t.k": api_key,  # Your API key
            "action": "jobs",  # API action for job search
            "q": keywords,  # Keywords for job search
            "l": location,  # Location for job search
        }

        response = requests.get(api_url, params=params)
        data = response.json()

        # Process and display job listings
        if "response" in data and "jobs" in data["response"]:
            jobs = data["response"]["jobs"]
            for job in jobs:
                print(f"Job Title: {job['jobtitle']}")
                print(f"Company: {job['company']}")
                print(f"Location: {job['location']}")
                print("--------")

# Usage example
glassdoor_tool = GlassdoorJobSearchingTool()
glassdoor_tool.search_jobs("software engineer", "San Francisco")
