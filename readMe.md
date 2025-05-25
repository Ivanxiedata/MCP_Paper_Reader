🧠 ArXiv Chatbot with Tool-Augmented Reasoning
This is a conversational AI assistant powered by ollama and augmented with custom tools for interacting with academic papers from arXiv. Ask it questions about research topics, and it will smartly retrieve, store, and extract information from papers — with tool use handled automatically under the hood.

🚀 Features
Natural Chat Interface with memory/history.

Tool-Augmented Reasoning: When relevant, the chatbot auto-detects keywords in its own output and invokes custom tools (search_papers, extract_info) to assist.

Paper Search from arXiv.org via the arxiv Python library.

Paper Storage: Results are saved under structured topic directories as JSON.

Information Extraction by paper_id, even across multiple topic folders.

🧩 Project Structure
project-root/
│
├── chatbot.py                # Main chatbot class & loop
├── utils/
│   ├── search_paper.py       # Tool: search papers from arXiv and save them
│   ├── extract_info.py       # Tool: extract saved info for a given paper ID
│   └── tool_mapping.py       # Maps tool name → function
│
├── papers/                   # Automatically generated folder to store paper info
│   └── topic_name/
│       └── papers_info.json  # Metadata of papers by topic


🧠 Tool Logic
search_papers
Triggered when chatbot mentions search_papers.

Requires topic (e.g. "machine learning").

Fetches top arXiv papers and stores them as JSON files under papers/<topic>/.

extract_info
Triggered when chatbot mentions extract_info.

Requires paper_id (e.g. "2401.12345").

Searches all topic folders for that paper ID and returns the stored metadata.

Tool invocation is automatically handled inside the chatbot loop by detecting tool names in the assistant’s output and extracting the required arguments using simple pattern matching.


🛠️ How to Use
1. Install Dependencies
uv pip install -r requirements.txt

Requirements include:

ollama

arxiv

python-dotenv

2. Set Up Ollama
Make sure you have Ollama installed and a compatible model like llama3 pulled locally:
ollama pull llama3

3. Run the Chatbot
python chatbot.py


🔍 Example Conversation
You: Can you search_papers on generative AI?
Assistant: Sure! I will search for recent papers on the topic of generative AI using arXiv...
[Tool search_papers Result]: 2405.01234, 2405.05678, ...

You: extract_info for paper_id = 2405.01234
Assistant: Here’s what I found for paper 2405.01234:
{
  "title": "...",
  "authors": [...],
  ...
}

📁 Paper Storage Format
Each topic folder contains a single papers_info.json with structure:
{
  "2405.01234": {
    "title": "A Breakthrough in ...",
    "authors": ["Alice A.", "Bob B."],
    "summary": "...",
    "pdf_url": "...",
    "published": "2024-05-12"
  },
  ...
}

