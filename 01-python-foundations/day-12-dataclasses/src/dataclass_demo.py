from dataclasses import (
    asdict,
    dataclass,
    field,
)


@dataclass
class Document:
    document_id: str
    title: str
    content: str
    score: float


@dataclass
class AgentState:
    user_query: str
    current_step: str
    tool_calls: int = 0
    retrieved_documents: list[Document] = field(
        default_factory=list
    )

    def __post_init__(self) -> None:
        self.user_query = self.user_query.strip()
        self.current_step = self.current_step.strip()


def main() -> None:

    document_1 = Document(
        document_id="doc-001",
        title="Python Type Hints",
        content=(
            "Type hints describe expected data types."
        ),
        score=0.94
    )

    document_2 = Document(
        document_id="doc-002",
        title="Pydantic",
        content=(
            "Pydantic provides runtime data validation."
        ),
        score=0.91
    )

    state = AgentState(
        user_query="  Explain type hints  ",
        current_step="retrieval",
        retrieved_documents=[
            document_1,
            document_2
        ]
    )

    print("Agent State:")
    print(state)

    print("\nUser Query:")
    print(state.user_query)

    print("\nRetrieved Documents:")

    for document in state.retrieved_documents:
        print(
            f"- {document.title} "
            f"(score={document.score})"
        )

    print("\nAs Dictionary:")
    print(asdict(state))


if __name__ == "__main__":
    main()