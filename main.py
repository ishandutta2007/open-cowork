import os
import sys
from interpreter import interpreter

# Configure interpreter to use open-source model
interpreter.llm.model = "ollama/llama3"  # Change to your preferred model
interpreter.auto_run = False  # Set to True for auto-execution, but be careful
interpreter.offline = True

if len(sys.argv) > 1:
    folder = sys.argv[1]
    if os.path.isdir(folder):
        os.chdir(folder)
        print(f"Changed working directory to {folder}")
    else:
        print(f"Invalid folder: {folder}")
        sys.exit(1)
else:
    print("Please provide a folder path as argument.")
    sys.exit(1)

# Start the chat
interpreter.chat()
