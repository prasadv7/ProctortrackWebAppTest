import openai
from summarizer import Summarizer
import spacy
import json

openai.api_key = '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'

document_path = r'C:\Users\GOD\Desktop\document.json'

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import subprocess

    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")


def retrieve_information_from_document(document_text):
    summarizer_model = Summarizer()
    relevant_passages = summarizer_model(document_text, ratio=0.2)  # Adjust ratio as needed
    return relevant_passages


def generate_answer_with_gpt(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()


def get_user_input():
    return input("User: ").strip()


def print_bot_response(response):
    print("Bot:", response)


def format_answer(answer):
    lines = answer.split(' -')
    formatted_lines = [f"- {line.strip()}" for line in lines if line.strip()]
    return '\n'.join(formatted_lines)


def get_answer_from_document(question, document_data, log_file):
    for item in document_data['questions']:
        if question.lower() in item['question'].lower():
            log_file.write(f"Retrieved from JSON: {item['answer']}\n")
            return item['answer']

    return None


def get_answer_from_json(question, document_path, log_file):
    with open(document_path, 'r', encoding='utf-8') as file:
        document_data = json.load(file)

    document_answer = get_answer_from_document(question, document_data, log_file)

    if document_answer:
        return document_answer
    else:
        return None


def semantic_similarity_match(user_input, document_questions):
    user_doc = nlp(user_input)

    non_empty_document_questions = [doc for doc in document_questions if doc.strip()]

    if not non_empty_document_questions:
        return None

    similarity_scores = [(doc, user_doc.similarity(nlp(doc))) for doc in non_empty_document_questions]
    best_match = max(similarity_scores, key=lambda x: x[1])

    if best_match[1] > 0.8:
        return best_match[0]
    else:
        return None


def identify_user_intent(user_input, document_text, document_data, log_file):
    if any(ent.text.lower() in ["product", "pricing", "features"] for ent in nlp(user_input).ents):
        return 'product', None
    elif 'customer support' in user_input.lower():
        return 'customer_support', None
    elif 'system issue' in user_input.lower():
        return 'system_issue', None

    matched_question = semantic_similarity_match(user_input, document_text)

    if matched_question:
        return 'document', matched_question

    return 'general', None


def ask_user_options():
    print_bot_response("Bot: Hi there! How can I assist you today?")
    print_bot_response("Bot: Here are some options:")
    print_bot_response("Bot: 1. Get product information")
    print_bot_response("Bot: 2. Customer support")
    print_bot_response("Bot: 3. Report a system issue")
    user_input = get_user_input()

    if 'product' in user_input.lower():
        return 'product'
    elif 'customer support' in user_input.lower():
        return 'customer_support'
    elif 'system issue' in user_input.lower():
        return 'system_issue'
    else:
        return 'general'


def main():
    with open(document_path, 'r', encoding='utf-8') as file:
        document_data = json.load(file)

    log_file = open('bot_log.txt', 'a')  # Open log file in append mode

    user_intent = ask_user_options()
    matched_question = None  # Initialize matched_question

    if user_intent == 'general':
        print_bot_response("Bot: Okay, let's continue with your question.")
        while True:
            user_input = get_user_input()

            if user_input.lower() == 'exit':
                print_bot_response("Bot: Goodbye!")
                break

            if any(greeting_word in user_input.lower() for greeting_word in ['hi', 'hello']):
                print_bot_response("Bot: Hello! How can I help you today?")
                continue

            # Check if there is an answer in the JSON file
            document_answer = get_answer_from_json(user_input, document_path, log_file)
            if document_answer:
                print_bot_response(f"Bot: {document_answer}")
            else:
                user_intent, matched_question = identify_user_intent(user_input, document_data, document_data, log_file)

                if user_intent == 'product':
                    document_answer = get_answer_from_json(user_input, document_path, log_file)
                    if document_answer:
                        print_bot_response(f"Bot: {document_answer}")
                    else:
                        prompt = f"Document information: {document_data}\nUser question: {user_input}\n"
                        gpt_response = generate_answer_with_gpt(prompt)
                        log_file.write(f"Generated with GPT: {gpt_response}\n")
                        print_bot_response("Bot: " + gpt_response)  # Print GPT response
                elif user_intent == 'customer_support':
                    print_bot_response(
                        "Bot: For customer support, please contact our dedicated support team at support@example.org.")
                elif user_intent == 'system_issue':
                    print_bot_response(
                        "Bot: I'm sorry to hear that you're facing a system issue. Please provide more details so that I "
                        "can assist you better.")
                elif user_intent == 'document':
                    if matched_question is not None:
                        document_answer = get_answer_from_document(matched_question, document_data, log_file)
                        if document_answer:
                            print_bot_response(f"Bot: {document_answer}")
                        else:
                            print_bot_response("Bot: I couldn't find an answer to that question in the document.")
                    else:
                        prompt = f"User question: {user_input}\n"
                        gpt_response = generate_answer_with_gpt(prompt)
                        log_file.write(f"Generated with GPT: {gpt_response}\n")
                        print_bot_response("Bot: " + gpt_response)  # Print GPT response
                else:
                    prompt = f"User question: {user_input}\n"
                    gpt_response = generate_answer_with_gpt(prompt)
                    log_file.write(f"Generated with GPT: {gpt_response}\n")
                    print_bot_response("Bot: " + gpt_response)
    elif user_intent == 'product':
        print_bot_response("Bot: You selected 'Get product information'.")
        print_bot_response("Bot: Please ask any specific questions about the product, pricing, or features.")
        while True:
            user_input = get_user_input()

            if user_input.lower() == 'exit':
                print_bot_response("Bot: Goodbye!")
                break

            document_answer = get_answer_from_json(user_input, document_path, log_file)
            if document_answer:
                print_bot_response(f"Bot: {document_answer}")
            else:
                prompt = f"Document information: {document_data}\nUser question: {user_input}\n"
                gpt_response = generate_answer_with_gpt(prompt)
                log_file.write(f"Generated with GPT: {gpt_response}\n")
                print_bot_response(gpt_response)
    elif user_intent == 'customer_support':
        print_bot_response("Bot: You selected 'Customer support'.")
        print_bot_response(
            "Bot: For customer support, please contact our dedicated support team at support@example.org.")
    elif user_intent == 'system_issue':
        print_bot_response("Bot: You selected 'Report a system issue'.")
        print_bot_response(
            "Bot: I'm sorry to hear that you're facing a system issue. Please provide more details so that I can "
            "assist you better.")
        while True:
            user_input = get_user_input()

            if user_input.lower() == 'exit':
                print_bot_response("Bot: Goodbye!")
                break

            document_answer = get_answer_from_json(user_input, document_path, log_file)
            if document_answer:
                print_bot_response(f"Bot: {document_answer}")
            else:
                prompt = f"User question: {user_input}\n"
                gpt_response = generate_answer_with_gpt(prompt)
                log_file.write(f"Generated with GPT: {gpt_response}\n")
                print_bot_response(gpt_response)

    log_file.close()  # Close the log file


if __name__ == "__main__":
    main()
