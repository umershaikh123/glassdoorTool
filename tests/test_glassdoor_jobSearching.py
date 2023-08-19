import unittest
from unittest.mock import patch, MagicMock
from glassdoor_jobSearching import GlassdoorJobSearchingTool

class TestGlassdoorJobSearchingTool(unittest.TestCase):
    @patch("glassdoor_jobSearching.requests.get")
    def test_search_jobs(self, mock_get):
        # Create a mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "response": {
                "jobs": [
                    {
                        "jobtitle": "Software Engineer",
                        "company": "TechCo",
                        "location": "San Francisco, CA",
                        # Add more mock job data
                    }
                ]
            }
        }
        mock_get.return_value = mock_response

        # Create an instance of the tool and execute it
        glassdoor_tool = GlassdoorJobSearchingTool()
        glassdoor_tool.search_jobs("software engineer", "San Francisco")

        # Add your assertions here to check if the output matches the mock response

if __name__ == "__main__":
    unittest.main()
