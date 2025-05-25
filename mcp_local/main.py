import arxiv
import json
import os
from typing import List
from dotenv import load_dotenv
import anthropic


from utils.search_paper import search_papers
from utils.extract_info import extract_infos
from utils.chatbot import Chatbot

cb = Chatbot()
cb.chat_loop()

