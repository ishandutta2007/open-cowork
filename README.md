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

