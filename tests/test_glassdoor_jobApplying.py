import unittest
from unittest.mock import patch
from glassdoor_jobApplying import GlassdoorJobApplyingTool

class TestGlassdoorJobApplyingTool(unittest.TestCase):
    @patch("glassdoor_jobApplying.webdriver.Chrome")
    def test_apply_for_job(self, mock_chrome):
        mock_driver = mock_chrome.return_value
        mock_driver.get.return_value = None  # Mock the get method

        # Create an instance of the tool and execute it
        glassdoor_tool = GlassdoorJobApplyingTool()
        
        job_url = "https://www.glassdoor.com/job_url"
        resume_path = "path/to/resume.pdf"
        application_details = {
            "input_field_id": "Your application details",
            # Add more application details as needed
        }

        glassdoor_tool.apply_for_job(job_url, resume_path, application_details)

        # Add your assertions here to check if the interactions are as expected

if __name__ == "__main__":
    unittest.main()
