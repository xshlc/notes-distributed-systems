import os
import re
import sys


def replace_latex_delimiters(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    # Read the content of the file
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Replace \[ and \] with $$
    content = re.sub(r"\\\[", "$$", content)
    content = re.sub(r"\\\]", "$$", content)

    # Replace \( and \) with $, ensuring no extra spaces are added
    content = re.sub(r"\\\((\s*)(.*?)(\s*)\\\)", r"$\2$", content)

    # Write the modified content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"LaTeX delimiters in '{file_path}' have been successfully replaced.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python replace_latex_delimiters.py <path_to_markdown_file>")
    else:
        file_path = sys.argv[1]
        replace_latex_delimiters(file_path)
