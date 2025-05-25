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

4. Interact with the chatbot:
```bash

## Example Usage
User: Can you search for papers about large language models?
Assistant: [search_papers: large language models]
Found 3 papers:
- 2405.01234: "Advances in LLM Pretraining"
- 2405.05678: "Efficient LLM Fine-tuning"
- 2405.07890: "LLM Safety Alignment"

User: Show me details for paper 2405.01234
Assistant: [extract_info: 2405.01234]
Title: Advances in LLM Pretraining
Authors: Smith J., Doe A.
Summary: This paper presents...
PDF: https://arxiv.org/pdf/2405.01234