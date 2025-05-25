🧠 ArXiv Chatbot with Tool-Augmented Reasoning
A conversational AI assistant powered by Ollama, augmented with tools to interact with arXiv papers. Automatically retrieves, stores, and extracts research papers for you.

🚀 Features
Natural Chat Interface with memory/history.

Tool-Augmented Reasoning: Auto-detects and invokes tools (search_papers, extract_info) when needed.

arXiv Paper Search: Fetches papers via the arxiv Python library.

Structured Storage: Saves papers in topic-based JSON files.

Information Extraction: Retrieves metadata by paper_id across all topics.

🛠️ Setup
Install Dependencies:

sh
pip install ollama arxiv python-dotenv
Set Up Ollama:

sh
ollama pull llama3  # or another compatible model
▶️ Usage
Run the chatbot:

sh
python chatbot.py
Example Workflow
You: "Search for papers on generative AI."
Assistant:

[Tool: search_papers] Found 3 papers:  
- 2405.01234: "A Breakthrough in Generative Models"  
- 2405.05678: "Diffusion-Based Text-to-Image Synthesis"  
You: "Show details for paper 2405.01234."
Assistant:

json
{
  "title": "A Breakthrough in Generative Models",
  "authors": ["Alice A.", "Bob B."],
  "summary": "...",
  "pdf_url": "https://arxiv.org/pdf/2405.01234",
  "published": "2024-05-12"
}
📁 Project Structure
project-root/
├── chatbot.py                # Main chatbot loop
├── utils/
│   ├── search_paper.py       # arXiv search & storage tool
│   ├── extract_info.py       # Metadata extraction tool
│   └── tool_mapping.py       # Tool name → function mapping
└── papers/                   # Paper storage
    └── topic_name/
        └── papers_info.json  # Paper metadata by topic

🔧 Tools
search_papers
Trigger: Mentions of search_papers + topic (e.g., "machine learning").

Action: Fetches top arXiv papers, saves to papers/<topic>/papers_info.json.

extract_info
Trigger: Mentions of extract_info + paper_id (e.g., "2405.01234").

Action: Searches all topic folders for the paper and returns metadata.