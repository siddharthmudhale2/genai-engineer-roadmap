from pathlib import Path


def main():
    data_dir = Path("data")

    input_file = data_dir / "input.txt"
    output_file = data_dir / "output.txt"

    if not input_file.exists():
        print("Input file does not exist.")
        return

    content = input_file.read_text(
        encoding="utf-8"
    )

    print("Input File Content:")
    print(content)

    output_content = (
        "Processed Content\n"
        "-----------------\n"
        f"{content}"
    )

    output_file.write_text(
        output_content,
        encoding="utf-8"
    )

    print("\nOutput file created successfully.")


if __name__ == "__main__":
    main()