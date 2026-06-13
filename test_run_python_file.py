from functions.run_python_file import run_python_file

def main():
    print("Test 1: run_python_file('calculator', 'main.py')")
    result = run_python_file("calculator", "main.py")
    print(result)
    print("-" * 50)

    print("Test 2: run_python_file('calculator', 'main.py', ['3 + 5'])")
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)
    print("-" * 50)

    print("Test 3: run_python_file('calculator', 'tests.py')")
    result = run_python_file("calculator", "tests.py")
    print(result)
    print("-" * 50)

    print("Test 4: run_python_file('calculator', '../main.py')")
    result = run_python_file("calculator", "../main.py")
    print(result)
    print("-" * 50)

    print("Test 5: run_python_file('calculator', 'nonexistent.py')")
    result = run_python_file("calculator", "nonexistent.py")
    print(result)
    print("-" * 50)

    print("Test 6: run_python_file('calculator', 'lorem.txt')")
    result = run_python_file("calculator", "lorem.txt")
    print(result)
    print("-" * 50)


if __name__ == "__main__":
    main()