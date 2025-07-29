## Overview 

An MCP that connects to my desktop to scan for files, then uses a resume file and a job description file to create a new laTex file of my resume.

- This is a simple mcp that exposes the users desktop to claude allowing reading and writting of files in a standadised way

Install py mcp, and uv (Python package and project manager)
```bash
pip install mcp
pip install uv
```

To install (connect) in claude
```bash
uv run mcp install main.py
```

Alternatively, you can test it with the MCP Inspector:
```bash
uv run mcp dev main.py
```