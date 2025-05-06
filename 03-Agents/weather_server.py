from typing import List
from fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    return "It's always sunny in New York"

if __name__ == "__main__":
    # mcp.run(transport="stdio", host="127.0.0.1", port=8888)

    import asyncio
    asyncio.run(mcp.run_sse_async(host="localhost", port=8000, log_level="debug"))