import asyncio
from uuid import uuid4

from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.mcp import MCPAdapter
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver



mcp_adapter = MCPAdapter("http://127.0.0.1:8000/mcp")

async def main():

    async with mcp_adapter:
        tools = await mcp_adapter.list_tools()
        llm = ChatOllama(model="llama3.2:latest")

        agent = create_agent(
            model=llm,
            tools=tools,
            system_prompt="you are a helpful task management assistant",
            checkpointer=InMemorySaver()
        )

        config = {"configurable": {"thread_id": str(uuid4())}}
        human_question = "can you please help me"

        while human_question != "q":

            result = await agent.ainvoke({"messages" : [HumanMessage(content=human_question)]},config=config)

            print(result["messages"][-1].text)
            # tool inspection
        
            for message in result["messages"]:
                for tool_call in getattr(message, "tool_calls", []):
                    print("Tool called:", tool_call["name"])
                    print("Arguments:", tool_call["args"])

            human_question = input("please ask your question or type q to exit:\n")



if __name__ == "__main__":
    asyncio.run(main())