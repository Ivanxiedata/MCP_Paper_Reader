# ArXiv Chatbot with Tool-Augmented Reasoning

A conversational AI assistant powered by Ollama that retrieves, stores, and extracts information from arXiv papers automatically.

## Features
- **Natural chat interface** with conversation memory
- **Auto-tool invocation**: Detects when to use `search_papers` or `extract_info` tools
- **arXiv integration**: Searches and fetches academic papers
- **Structured storage**: Organizes papers by topic in JSON format
- **Paper lookup**: Finds papers by ID across all topics

## Quick Start
1. Install dependencies:
```bash
pip install ollama arxiv python-dotenv

2. Set up Ollama (requires Ollama installed):
ollama pull llama3

3.Run the chatbot:
python chatbot.py


