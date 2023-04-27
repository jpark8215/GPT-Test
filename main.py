import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "sk-xxxx"


# Initialize conversation flag
end_conversation = False

while not end_conversation:
    # Prompt the user for input
    prompt = input("What would you like to ask OpenAI? ")

    # Call OpenAI's API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.9)

    # Extract the response from the API call
    answer = response.choices[0].text.strip()

    # Display the response to the user
    print("OpenAI's response: \n" + answer)

    # Ask the user if they have another question
    another_question = input("Do you have another question? (y/n) ")

    if another_question.lower() == "n":
        # Ask the user if they want to end the conversation
        end_chat = input("Are you sure to end the conversation? (y/n) ")

        if end_chat.lower() == "y":
            end_conversation = True
