import openai

# Set up OpenAI API key
openai.api_key = ""

# List of questions to ask
questions = [
    "How effectively did the senior accountant manage financial reporting deadlines?",
    "How accurate was their financial reporting?"
]

# Define the output file to save the responses
output_file = "data/questions_answers.txt"

def get_response(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": (
                    "You are assisting an HR Manager conducting an employee interview "
                    "for the role of a Senior Accountant. For each question, provide 4 multiple-choice options "
                    "labeled A, B, C, and D that are concise and suitable for HR documentation."
                )},
                {"role": "user", "content": question}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    with open(output_file, "w") as file:
        for idx, question in enumerate(questions, start=1):
            print(f"Asking question {idx}/{len(questions)}: {question}")
            answer = get_response(question)
            file.write(f"Question {idx}: {question}\n")
            file.write(f"Answer: {answer}\n\n")
            print(f"Answer saved for question {idx}\n")
    print(f"All responses saved to {output_file}")

if __name__ == "__main__":
    main()
