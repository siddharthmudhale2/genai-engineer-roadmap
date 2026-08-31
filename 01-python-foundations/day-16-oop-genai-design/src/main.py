from .providers import (
    CloudLLMProvider,
    LocalLLMProvider,
)
from .services import ChatService


def main() -> None:

    cloud_provider = CloudLLMProvider(
        model="cloud-demo-model"
    )

    local_provider = LocalLLMProvider(
        model="local-demo-model"
    )

    cloud_chat = ChatService(
        provider=cloud_provider
    )

    local_chat = ChatService(
        provider=local_provider
    )

    prompt = (
        "Explain dependency injection"
    )

    print("Cloud Provider:")
    print(
        cloud_chat.chat(prompt)
    )

    print()

    print("Local Provider:")
    print(
        local_chat.chat(prompt)
    )


if __name__ == "__main__":
    main()