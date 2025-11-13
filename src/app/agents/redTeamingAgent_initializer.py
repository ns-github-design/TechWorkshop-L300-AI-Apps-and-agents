# Azure imports
from azure.identity import DefaultAzureCredential
from azure.ai.evaluation.red_team import RedTeam, RiskCategory, AttackStrategy
from pyrit.prompt_target import OpenAIChatTarget
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

# Azure AI Project Information
azure_ai_project = os.getenv("AZURE_AI_AGENT_ENDPOINT")

# Instantiate your AI Red Teaming Agent
red_team_agent = RedTeam(
    azure_ai_project=azure_ai_project,
    credential=DefaultAzureCredential(),
    risk_categories=[
        RiskCategory.Violence,
        RiskCategory.HateUnfairness,
        RiskCategory.Sexual,
        RiskCategory.SelfHarm
    ],
    num_objectives=5, 
)

# Configuration for Azure OpenAI model
azure_openai_config = {
    "azure_endpoint": os.environ.get("AZURE_OPENAI_ENDPOINT"),
    "api_key": os.environ.get("AZURE_OPENAI_KEY"),
    "azure_deployment": os.environ.get("AZURE_OPENAI_API_VERSION"),
}

async def main():
    print("Running red team scan...")

    # REQUIRED CHANGE FROM INSTRUCTIONS:
    red_team_result = await red_team_agent.scan(target=azure_openai_config)

    print("Red team scan completed.")
    print(red_team_result)

# Run main
asyncio.run(main())

