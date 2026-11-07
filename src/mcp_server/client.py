import asyncio

from fastmcp import Client
from fastmcp.exceptions import ToolError

client = Client("http://127.0.0.1:8000/mcp")

async def get_tools_from_server():
    async with client:
        tools = await client.list_tools()

        # printing tools
        for tool in tools:
            print(tool.name)

    return tools

async def create_task_using_mcp():
    async with client:
        result = await client.call_tool(
            "create_task",
            {
            "title": "Record MCP Tutorial",
            "priority": "high",
            "description": "Create a YouTube tutorial about MCP"
            }
        )

        print(result.data)
        
    return result.data

async def update_task_status_from_mcp():
    async with client:
        print("testing update normally")
        result = await client.call_tool(
            "update_task_status",
            {
                "task_id": "9a4a29bc-7b88-458c-b71c-cde3bd8d4b10", 
                "status": "IN-PROGRESS"
            }
        )
        print(result.data)

    return result.data

async def list_tasks_using_mcp():
    async with client:
        result = await client.call_tool(
            "list_tasks"
        )

        print("these are all the tasks:")
        print(result.data)

    return result.data

if __name__ == "__main__":
    asyncio.run(get_tools_from_server())
    asyncio.run(list_tasks_using_mcp())
    asyncio.run(create_task_using_mcp())
    asyncio.run(list_tasks_using_mcp())
    asyncio.run(update_task_status_from_mcp())
    asyncio.run(list_tasks_using_mcp())
    