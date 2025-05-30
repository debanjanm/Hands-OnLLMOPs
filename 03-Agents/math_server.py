from fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    # mcp.run(transport="sse")

    import asyncio
    asyncio.run(mcp.run_sse_async(host="localhost", port=9000, log_level="debug"))