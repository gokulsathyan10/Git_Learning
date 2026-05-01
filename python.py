import os

def run_python_code(code):
    with open("README.md", "w") as f:
        f.write(code)


if __name__ == "__main__":
    code = input("Enter your text: ")
    run_python_code(code)