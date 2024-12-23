import json

# Function to extract questions and answers from the file
def extract_qna(input_file, output_file):
    questions = []
    answers = []

    # Open and read the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                try:
                    data = json.loads(line)
                    text = data.get("text", "")

                    # Extract the question and answer
                    if "[INST]" in text and "[/INST]" in text:
                        question = text.split("[INST]")[1].split("[/INST]")[0].strip()
                        answer = text.split("[/INST]")[1].strip()
                        questions.append(question)
                        answers.append(answer)
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON line: {line}")

    # Write the questions and answers to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("QUESTION\n")
        file.write("\n\n".join(questions))
        file.write("\n\nANSWERS\n")
        file.write("\n\n".join(answers))

# Input and output file paths
input_file = 'input.txt'  # Replace with the path to your input file
output_file = 'output.txt'  # Replace with the desired output file path

# Extract questions and answers
extract_qna(input_file, output_file)

print("Questions and answers have been extracted and saved to", output_file)
