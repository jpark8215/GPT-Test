import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "sk-O"


# Set the initial prompt
prompt = "Hello."

# Loop to keep the conversation going
while True:
    # Call OpenAI's API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    # Extract the response from the API call
    answer = response.choices[0].text.strip()

    # Display the response to the user
    print("OpenAI's response: " + answer)

    # Update the prompt for the next iteration
    prompt = input()

    # Check if the user wants to end the conversation
    if prompt.lower() in ["exit", "quit", "bye", "goodbye"]:
        break

# Initialize conversation-ending flag
end_conversation = False

while not end_conversation:
    # Ask the user if they have another question
    another_question = input("Do you have another question? (y/n) ")

    if another_question.lower() == "n":
        # Ask the user if they want to end the conversation
        end_chat = input("Are you sure to end the conversation? (y/n) ")

        if end_chat.lower() == "y":
            end_conversation = True
        elif end_chat.lower() == "n":
            # User changed their mind about ending the conversation
            pass
        else:
            print("Sorry, I didn't understand that. Please enter 'y' for yes or 'n' for no.")

    elif another_question.lower() == "y":
        # User has another question, so prompt for it
        prompt = input("What's your question? ")

        # Call OpenAI's API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.9)

        # Extract the response from the API call
        answer = response.choices[0].text.strip()

        # Display the response to the user
        print("OpenAI's response: \n" + answer)

        # Update the prompt for the next iteration
        prompt = input()

        # Check if the user wants to end the conversation
        if prompt.lower() in ["exit", "quit", "bye", "goodbye", "ok", "thanks"]:
            break

    else:
        print("Sorry, I didn't understand that. Please enter 'y' for yes or 'n' for no.")
