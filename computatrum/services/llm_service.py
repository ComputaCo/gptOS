from langchain.schema import BaseLanguageModel

from computatrum.services.base_service import Service
from computatrum.utils.singleton import Singleton


class LLMService(Service, Singleton):
    """
    - Provides fault tolerant abstraction layer for multiple LLMs
    - Records all API requests and responses (json and human readable conversation)
    - Tracks cost of total usages of LLMs
    """
