# Open Cowork

An open-source alternative to Claude Cowork, powered by Open Interpreter.

## Setup

1. Install Ollama: https://ollama.com

2. Run `ollama run llama3`

3. pip install -r requirements.txt

4. python main.py /path/to/your/workspace

5. Chat with the agent to perform tasks in the workspace.

## Features

- Workspace scoping: All operations are performed within the specified folder.

- Permission handling: Prompts user before executing code or system commands.

- Live interaction: Real-time chat with the AI agent.

- Extensible: Uses Open Interpreter, which supports plugins and custom skills.


- Direct File Access: Users designate a specific local folder on their Mac. Claude can read, create, edit, rename, and organize files within that folder autonomously.
- Autonomous Task Execution: Unlike standard chat, Cowork acts on high-level goals (e.g., "organize these downloads by project"). It creates a plan, breaks it into subtasks, and executes them without constant human prompting.
- Professional Outputs: Claude can generate polished deliverables, including Excel spreadsheets with working formulas, PowerPoint presentations, and formatted reports from scattered notes or images.
- Web-Based Tasks: When paired with the "Claude in Chrome" extension, Cowork can navigate websites, gather information, and perform web-based actions like checking emails or updating dashboards.
- Third-Party Connectors: It integrates with external tools like Notion, Asana, GitHub, Slack, and Salesforce to pull or push data.
- Parallel Processing: Claude can coordinate multiple "sub-agents" to work on different parts of a complex task simultaneously.


