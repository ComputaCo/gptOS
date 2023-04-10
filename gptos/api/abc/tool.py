from typing import runtime_checkable
import attr


@runtime_checkable
class Tool:
    """Must include docstring for description."""

    def __call__(self, input: str) -> None:
        ...
        
    @staticmethod
    def __render


@attr.s(auto_attribs=True)
class Toolbox(Tool):
    name: str = attr.ib()
    description: str = attr.ib()
    tools: list[Tool] = attr.ib([])

    def func(self, input) -> str:
        return "Select:" + "\t".join(
            [f"{tool.name}: {tool.description}" for tool in self.tools]
        )
