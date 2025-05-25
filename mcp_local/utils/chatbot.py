import os
from dotenv import load_dotenv
from utils.tool_mapping import execute_tool
import ollama

class Chatbot:
    def __init__(self, model="llama3"):
        # load_dotenv()
        self.model = model
        self.history = []

        self.tools = {
            "search_papers": {
                "description": "Search for papers on arXiv based on a topic and store their information.",
                "required": ["topic"]
            },
            "extract_info": {
                "description": "Search for information about a specific paper across all topic directories.",
                "required": ["paper_id"]
            }
        }

    def process_query(self, query):
        self.history.append({"role": "user", "content": query})

        response = ollama.chat(
            model=self.model,
            messages=self.history,
        )

        reply = response['message']['content']
        print(f"\nAssistant: {reply}")
        self.history.append({"role": "assistant", "content": reply})

        # (Optional) Tool detection (naive version based on keywords)
        for tool_name, tool_info in self.tools.items():
            if tool_name in reply:
                try:
                    args = self.extract_tool_args(reply, tool_info["required"])
                    result = execute_tool(tool_name, args)
                    print(f"[Tool {tool_name} Result]: {result}")
                    self.history.append({"role": "user", "content": f"Tool result: {result}"})
                except Exception as e:
                    print(f"[Tool Error]: {str(e)}")

    def extract_tool_args(self, message, required_keys):
        # Naive JSON-like extraction from message for demo purposes
        import re
        args = {}
        for key in required_keys:
            match = re.search(rf"{key}\s*[:=]\s*['\"]?([^,'\".\n]+)", message, re.IGNORECASE)
            if match:
                args[key] = match.group(1)
        return args

    def chat_loop(self):
        print("Type your queries or 'quit' to exit.")
        while True:
            try:
                query = input("\nEnter Your Query: (Or type 'quit' or 'q' to exit)" ).strip()
                if query.lower() == 'quit' or query.lower() == 'q':
                    break
                self.process_query(query)
            except Exception as e:
                print(f"Error: {e}")

