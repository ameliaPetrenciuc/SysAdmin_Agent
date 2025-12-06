from dotenv import load_dotenv 
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset, StreamableHTTPConnectionParams
from google.adk.models.lite_llm import LiteLlm
from pathlib import Path

load_dotenv()  
OLLAMA_MODEL="ollama_chat/llama3.2:latest"
OLLAMA_SERVICE_URL="http://ollama:11434"

def get_sysadmin_agent():

    sysadmin_tool_set = McpToolset(
        connection_params=StreamableHTTPConnectionParams(
            url="http://mcp-server:8002/mcp"
        )
    )

    instruction = Path(__file__).with_name("instructions.txt").read_text()

    agent_sys = Agent(
        name="SysAdmin_Agent",
        description="An agent that helps with system administration tasks by using tools to inspect and read files in a managed directory.",
        instruction=instruction,
        model=LiteLlm(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_SERVICE_URL,
            model_config={ 
                "temperature": 0.1,
                "top_p": 0.9,
                "max_tokens": 4096,
            },
        ),
        tools=[sysadmin_tool_set],
    )
    return agent_sys

root_agent = get_sysadmin_agent()
    