from pydantic import BaseModel, Field
from google.adk.agents.llm_agent import LlmAgent


class EmailContent(BaseModel):
    """Blueprint for email outputs"""
    subject: str = Field(
        description="Concise, descriptive subject line (5-10 words)"
    )
    body: str = Field(
        description="Formatted content with greeting, paragraphs, and signature"
    )

root_agent = LlmAgent(
    name="email_agent",
    model="gemini-2.0-flash",
    instruction="""
    Generate professional emails with:
    - Clear subject line
    - Proper greeting/closing
    - Well-structured body
    Response MUST be JSON matching EmailContent schema
    """,
    output_schema=EmailContent,
    output_key="email",
)
