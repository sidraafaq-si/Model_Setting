from agents import Agent, Runner, function_tool, ModelSettings
from connection import config
import asyncio
from agents.agent import StopAtTools

#@function_tool
#def get_weather(city: str) -> str:
  #  print("Present Sir !")
   # """
   # Fetches weather for a given city (dummy tool).
    #"""
   # return f"The weather in {city} is sunny."

#agent = Agent(
    #name="Weather Assistant",
    #instructions="You are an assistant that provides weather information. "
      #           "Use the get_weather tool whenever the user asks about the weather.",
    #tools=[get_weather],
    #model_settings=ModelSettings(
      #  temperature=0.1,
       # max_tokens=50,
        #tool_choice="required"

    #),

    #tool_use_behavior="stop_on_first_tool"
#)

#result = Runner.run_sync(agent, "Hi", run_config=config)

@function_tool
def add (a: int, b: int) -> int:
    return a + b + 6

agent = Agent(
    name="Math Assistant",
    instructions="you help users with math problems. Use the available tools to provide the accurate responses.",
    tools=[add],
    tool_use_behavior=StopAtTools(stop_at_tools_names=["add"]),
    model_settings=ModelSettings(
        temperature=0.1,
        max_tokens=50,
        tool_choice="add"
    )
)

async def main():
    result = await Runner.run(agent, "What is 2+2?", run_config=config)
    print(result.final_output)

if(__name__ == "__main__"):
    asyncio.run(main())








