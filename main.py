
# server.py
import os
from mcp.server.fastmcp import FastMCP
from mcp import types
import mcp.types
# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


@mcp.tool(
    name="read-latex-tool",
    description="Read a LaTex file",
)
async def readLaTex(fileName: str) -> str:
    """Read a LaTex file and return its content"""
    # open files in desktop
    url = rf'C:\Users\YABOIMARSH\Desktop\{fileName}'
    try:
        with open(url, "r") as doc:
            content = []
            for para in doc.readlines():
                content.append(para.strip())
            return "\n".join(content)
    except FileNotFoundError:
        return "File not found"
    
@mcp.tool(
    name="write-latex-tool",
    description="Write a LaTex file",
    
)
async def writeLaTex(fileName: str, content: str) -> None:
    """Write content to a NEW LaTex file"""
    # open files in desktop
    url = rf"C:\Users\YABOIMARSH\Desktop\{fileName}"
    doc = open(url, "w")
    doc.write(content)
    doc.close()
    return

@mcp.tool(
    name="read-txt-tool",
    description="Read a text file",
)   
async def readTxtFile(fileName: str) -> str:
    """Read a text file and return its content"""
    # open files in desktop
    url = rf'C:\Users\YABOIMARSH\Desktop\{fileName}'
    try:
        with open(url, "r") as doc:
            content = []
            for para in doc.readlines():
                content.append(para.strip())
            return "\n".join(content)
    except FileNotFoundError:
        return "File not found"
    return "\n".join(content)


@mcp.resource("desktop://data")
def getData() -> str:
    """desktop data """
    try:
        files = os.listdir(r'C:\Users\YABOIMARSH\Desktop\\')
        return str({"files": files})
    except Exception as e:
        return str({"error": str(e)})



@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    return "App configuration here"


@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: str) -> str:
    """Dynamic user data"""
    return f"Profile data for user {user_id}"
"""Dont scrape i got banned from indeed"""


if __name__ == "__main__":
    mcp.run(transport="stdio")
    