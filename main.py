
# server.py
import os
from mcp.server.fastmcp import FastMCP
# Create an MCP server
mcp = FastMCP("Demo")


@mcp.tool(
    name="read-latex-tool",
    description="Read a LaTex file",
)
async def readLaTex(fileName: str) -> str:
    """Read a LaTex file and return its content"""
    # open files in desktop
    username = os.getlogin()    # Fetch usernam
    url = rf'C:\Users\{username}\Desktop\{fileName}'
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
    username = os.getlogin()    # Fetch usernam
    url = rf'C:\Users\{username}\Desktop\{fileName}'
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
    username = os.getlogin()    # Fetch usernam
    url = rf'C:\Users\{username}\Desktop\{fileName}'
    try:
        with open(url, "r") as doc:
            content = []
            for para in doc.readlines():
                content.append(para.strip())
            return "\n".join(content)
    except FileNotFoundError:
        return "File not found"
    return "\n".join(content)


@mcp.tool(
    name="read-desktop",
    description="reads the desktop",
) 
def read_users_desktop_tool() -> str:
    try:
        username = os.getlogin()    # Fetch usernam
        url = rf'C:\Users\{username}\Desktop'
        files = os.listdir(url)
        return str({"files": files})
    except Exception as e:
        return str({"error": str(e)})


@mcp.resource(
    uri ="desktop://data",
    name='read-desktop-data',
    description='Connects to the users desktop and reads name of all the files'
    )
def read_desktop_data() -> str:
    """desktop data """
    try:
        username = os.getlogin()    # Fetch usernam
        url = rf'C:\Users\{username}\Desktop'
        files = os.listdir(url)
        return str({"files": files})
    except Exception as e:
        return str({"error": str(e)})



if __name__ == "__main__":

    mcp.run(transport="stdio")
     