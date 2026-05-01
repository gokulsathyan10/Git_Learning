def run_test_code(code):
    with open("TEST.md", "w") as f:
        f.write(code)


if __name__ == "__main__":
    code = input("Enter your test code: ")
    run_test_code(code)