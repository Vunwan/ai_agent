from functions.write_file import write_file

def main() -> None:
    working_dir = "calculator"

    print("\n--- overwrite existing file ---")
    result1 = write_file(
        working_dir,
        "lorem.txt",
        "wait, this isn't lorem ipsum"
    )
    print(result1)

    print("\n--- write to nested new file ---")
    result2 = write_file(
        working_dir,
        "pkg/morelorem.txt",
        "lorem ipsum dolor sit amet"
    )
    print(result2)

    print("\n--- attempt outside working directory ---")
    result3 = write_file(
        working_dir,
        "/tmp/temp.txt",
        "this should not be allowed"
    )
    print(result3)


if __name__ == "__main__":
    main()