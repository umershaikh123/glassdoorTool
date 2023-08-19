from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List

# Import your custom tools
from glassdoor_jobSearching import GlassdoorJobSearchingTool
from glassdoor_jobApplying import GlassdoorJobApplyingTool

class GlassdoorToolkit(BaseToolkit):
    name: str = "Glassdoor Toolkit"
    description: str = "Custom toolkit for job searching and applying on Glassdoor.com"

    def get_tools(self) -> List[BaseTool]:
        # Return instances of your custom tools
        return [GlassdoorJobSearchingTool(), GlassdoorJobApplyingTool()]

    def get_env_keys(self) -> List[str]:
        # If you need environment keys for your tools, specify them here
        return ["YOUR_ENV_KEY_1", "YOUR_ENV_KEY_2"]
