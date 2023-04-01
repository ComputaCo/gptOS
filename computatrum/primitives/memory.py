from computatrum.primitives.embedding import Embedding
from computatrum.services.llm_service import LLMService


class Memory:  # eveything that goes in the memory should subclass this
    def embed(self) -> Embedding:
        return LLMService.Singleton().embed(str(self))
