# Model_Setting
Math Assistant

This project demonstrates how to build an AI-powered assistant that can use tools to solve problems. It is based on the Agent, Runner, and function_tool abstractions, allowing you to define tools, wrap them in an agent, and run conversations with them.

Features

Define custom tools using @function_tool.

Create agents with specific instructions and behaviors.

Run agents synchronously or asynchronously with Runner.

Example implementation: a math assistant that adds numbers.

Project Structure . ├── agents/ # Agent framework (Agent, Runner, etc.) ├── connection/ # Configurations (API keys, settings) ├── main.py # Example math assistant implementation └── README.md # Project documentation

Example Code from agents import Agent, Runner, function_tool, ModelSettings from connection import config import asyncio

@function_tool def add(a: int, b: int) -> int: return a + b

agent = Agent( name="Math Assistant", instructions="You help users with math problems. Use the available tools to provide accurate responses.", tools=[add], model_settings=ModelSettings( temperature=0.1, max_tokens=50, tool_choice="auto" ) )

async def main(): result = await Runner.run(agent, "What is 2+2?", run_config=config) print("Final Output:", result.final_output)

if name == "main": asyncio.run(main())

Running the Project

Install dependencies (make sure you have Python 3.10+):

pip install -r requirements.txt

Set up your connection/config.py with API credentials or model configuration.

Run the example:

python main.py

Customization

Add new tools by defining functions with the @function_tool decorator.

Change agent behavior via ModelSettings (temperature, max tokens, tool choice).

Switch between Runner.run (async) and Runner.run_sync (sync) depending on your application.
