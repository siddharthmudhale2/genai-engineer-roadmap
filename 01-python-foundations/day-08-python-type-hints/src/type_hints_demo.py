from typing import TypedDict


class UserProfile(TypedDict):
    name: str
    age: int
    skills: list[str]


def calculate_score(
    marks: list[int]
) -> float:
    return sum(marks) / len(marks)


def get_skills() -> list[str]:
    return [
        "Python",
        "FastAPI",
        "Generative AI"
    ]


def find_role(
    experience: int
) -> str | None:

    if experience >= 1:
        return "AI Engineer"

    return None


def create_profile(
    name: str,
    age: int,
    skills: list[str]
) -> UserProfile:

    return {
        "name": name,
        "age": age,
        "skills": skills
    }


def main() -> None:

    marks: list[int] = [
        85,
        90,
        88
    ]

    score: float = calculate_score(marks)

    skills: list[str] = get_skills()

    role: str | None = find_role(1)

    profile: UserProfile = create_profile(
        "Siddharth",
        25,
        skills
    )

    print("Score:", score)
    print("Skills:", skills)
    print("Role:", role)
    print("Profile:", profile)


if __name__ == "__main__":
    main()