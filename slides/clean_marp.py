import re
import sys
import os

def clean_marp_slides(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    cleaned_lines = []
    presenter_notes = []
    in_presenter_notes = False

    for line in lines:
        # Detect start and end of presenter notes
        if "<!--presenter notes" in line:
            in_presenter_notes = True
            presenter_notes.append(line)
            continue
        if "-->" in line and in_presenter_notes:
            in_presenter_notes = False
            presenter_notes.append(line)
            # Add presenter notes after the image and caption
            cleaned_lines.append("".join(presenter_notes))
            presenter_notes = []
            continue

        # Add presenter notes lines
        if in_presenter_notes:
            presenter_notes.append(line)
            continue
        
        # Detect image line
        if line.startswith("![]"):
            # Move the image and caption together
            cleaned_lines.append(line)
            continue

        # Add captions as plain text (assuming captions follow immediately after images)
        cleaned_lines.append(line)

    # Write cleaned content to the output file
    with open(output_file, 'w', encoding='utf-8') as output:
        output.writelines(cleaned_lines)

    print(f"Slides cleaned and written to {output_file}")

if __name__ == "__main__":
    # Check if the user passed a file as an argument
    if len(sys.argv) < 2:
        print("Usage: python clean_marp.py <input_markdown_file>")
        sys.exit(1)
    
    # Get the input file from command line
    input_file = sys.argv[1]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: The file {input_file} does not exist.")
        sys.exit(1)
    
    # Set the output file name by appending '_cleaned' to the input file name, keeping .md extension
    output_file = f"{os.path.splitext(input_file)[0]}_cleaned.md"
    
    # Run the cleaning function
    clean_marp_slides(input_file, output_file)
