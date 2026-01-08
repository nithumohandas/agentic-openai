from typing import Dict

from agents import Agent, function_tool
from model import Model


@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Dummy function to send an email"""
    print("Email response", html_body)
    return "success"


INSTRUCTIONS = """You are able to send a nicely formatted text email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model=Model.gemini_model,
)
