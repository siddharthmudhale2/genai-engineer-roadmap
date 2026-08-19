from pydantic import BaseModel, Field, ValidationError


class User(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50
    )

    age: int = Field(
        ge=18,
        le=100
    )

    skills: list[str]


def main() -> None:

    user = User(
        name="Siddharth",
        age=25,
        skills=[
            "Python",
            "FastAPI",
            "Generative AI"
        ]
    )

    print("Valid User:")
    print(user)

    print("\nAs Dictionary:")
    print(user.model_dump())

    print("\nAs JSON:")
    print(user.model_dump_json())

    print("\nTesting Invalid Data:")

    try:
        User(
            name="A",
            age=10,
            skills="Python"
        )

    except ValidationError as error:
        print(error)


if __name__ == "__main__":
    main()