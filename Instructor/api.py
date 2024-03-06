import json

document_path = r'C:\Users\GOD\Desktop\document.json'  # Replace with the actual path to your JSON document

def get_answer_from_document(question, document_data):
    for item in document_data['questions']:
        if question.lower() in item['question'].lower():
            return item['answer']

    return "I'm sorry, but I couldn't find relevant information for your question."

def get_user_input():
    return input("User: ")

def print_bot_response(response):
    print("Bot:\n", response)

def format_answer(answer):
    # Split the answer into lines based on the hyphen (-) followed by a space
    lines = answer.split(' -')
    formatted_lines = [f"- {line.strip()}" for line in lines if line.strip()]
    return '\n'.join(formatted_lines)

def main():
    with open(document_path, 'r', encoding='utf-8') as file:
        document_data = json.load(file)

    while True:
        user_input = get_user_input()

        if user_input.lower() == 'exit':
            print_bot_response("Bot: Goodbye!")
            break

        if any(greeting_word in user_input.lower() for greeting_word in ['hi', 'hello']):
            print_bot_response("Bot: Hello! How can I help you today?")
            continue

        # Try to get an answer from the document
        document_answer = get_answer_from_document(user_input, document_data)

        if document_answer:
            formatted_answer = format_answer(document_answer)
            print_bot_response(f"{formatted_answer}")
        else:
            print_bot_response("Bot: I couldn't find an answer to that question in the document.")
if __name__ == "__main__":
    main()
