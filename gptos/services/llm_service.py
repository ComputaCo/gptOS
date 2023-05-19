from langchain.schema import BaseLanguageModel

from computatrum.services.base_service import Service
from gptos.api.misc.singleton import Singleton


class LLMService(Service, Singleton):
    """
    This is used inside the

    - Provides fault tolerant abstraction layer for multiple LLMs
    - Records all API requests and responses (json and human readable conversation)
    - Tracks cost of total usages of LLMs
    """

    def llm(self, difficulty) -> BaseLanguageModel:
        ...

    def embed(self, str):
        ...
