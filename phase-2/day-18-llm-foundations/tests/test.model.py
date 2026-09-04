from src.model import DemoLLM


def test_model_generation():

    model = DemoLLM()

    result = model.generate(
        "Hello world"
    )

    assert (
        "Received 2 tokens"
        in result
    )


def test_custom_model_name():

    model = DemoLLM(
        model_name="test-model"
    )

    result = model.generate(
        "Hello"
    )

    assert (
        "[test-model]"
        in result
    )