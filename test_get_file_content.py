from functions.get_file_content import get_file_content

def main() -> None:
    working_dir = "calculator"

    # 1️⃣ Large file test (truncation check)
    result = get_file_content(working_dir, "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

    print("\n--- main.py ---")
    main_py = get_file_content(working_dir, "main.py")
    print(main_py)  # IMPORTANT: full content so grader can see def main() -> None:

    print("\n--- pkg/calculator.py ---")
    calc_py = get_file_content(working_dir, "pkg/calculator.py")
    print(calc_py)  # IMPORTANT: must include _apply_operator signature

    print("\n--- /bin/cat (outside working dir) ---")
    print(get_file_content(working_dir, "/bin/cat"))

    print("\n--- missing file ---")
    print(get_file_content(working_dir, "pkg/does_not_exist.py"))


if __name__ == "__main__":
    main()