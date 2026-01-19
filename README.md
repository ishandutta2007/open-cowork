# Open Cowork

An open-source alternative to Claude Cowork, powered by Open Interpreter (assuming 'OpenCode' refers to similar open-source code interpreters).

This is a simple CLI tool that allows an AI agent to perform tasks in a specified folder using Open Interpreter.

## Installation

1. Install Open Interpreter: `pip install open-interpreter`
2. Install Ollama and pull a model, e.g., `ollama pull llama3`
3. Run Ollama server: `ollama serve`

## Usage

python main.py /path/to/your/folder

Then, interact with the chat to describe tasks. The agent can run code, edit files, etc., in the folder.
