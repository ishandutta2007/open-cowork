import os
import argparse
from interpreter import interpreter

def main():
    parser = argparse.ArgumentParser(description="Open Cowork CLI")
    parser.add_argument("folder", help="Path to workspace folder")
    args = parser.parse_args()
    if not os.path.isdir(args.folder):
        print("Invalid folder path.")
        return
    os.chdir(args.folder)
    interpreter.llm.model = "ollama/llama3"
    interpreter.auto_run = False  # Require user confirmation for runs
    interpreter.safe_mode = "ask"  # Or "auto" but ask for safety
    print("Starting Open Cowork chat. Type 'exit' to quit.")
    interpreter.chat()

if __name__ == "__main__":
    main()
