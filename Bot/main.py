import json
import re

from Bot import error
from Bot import api


# Load JSON data
def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


# Store JSON data
response_data = load_json("Bot/logic.json")


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required score
        if required_score == len(required_words):
            # print(required_score == len(required_words))
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase
        # print(response_score, response["user_input"])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # If there is no good response, return a random one.
    if best_response != 0:

        answer = response_data[response_index]["bot_response"]

        if answer == 'placeholder':
            response_type = response_data[response_index]["response_type"]
            answer = placeholder(user_input, response_type)

        else:
            answer = response_data[response_index]["bot_response"]

        return answer

    return error.error_response()


# returns the last word in a sentence
def lastWord(string):

    lis = list(string.split(" "))
    length = len(lis)

    return lis[length - 1]


# returns the first word in a sentence
def firstWord(string):

    lis = list(string.split(" "))

    unwanted = ["a", "the", "is"]

    new_words = [word for word in lis if word not in unwanted]
    return new_words[0]


# returns the word that comes after use
def useWOrd(sentence):
    lis = list(sentence.split(" "))

    for i in range(len(lis)):
        if lis[i].lower() == 'use':
            return lis[i + 1]


# function gives an appropriate response for any logic that has "placeholder" as a response.
def placeholder(question, response_type):

    if response_type == 'definition':
        answer = lastWord(question)

        define = api.wordAPI_define(answer)
        return define

    if response_type == 'partOF':
        answer = firstWord(question)

        part_of = api.wordAPI_partOf(answer)
        return part_of

    if response_type == 'antonym':
        answer = lastWord(question)

        antonym = api.wordAPI_antonyms(answer)
        return antonym

    if response_type == 'synonyms':
        answer = lastWord(question)

        synonyms = api.wordAPI_synonyms(answer)
        return synonyms

    if response_type == 'syllables':
        answer = lastWord(question)

        syllables = api.wordAPI_syllables(answer)
        return syllables

    if response_type == 'pronunciation':
        answer = lastWord(question)

        pronunciation = api.wordAPI_pronunciation(answer)
        return pronunciation

    if response_type == 'example':
        answer = useWOrd(question)

        example = api.wordAPI_examples(answer)
        return example

    if response_type == 'everything':
        answer = lastWord(question)

        everything = api.wordAPI_everything(answer)
        return everything

    if response_type == 'help':

        answer = error.help_me()
        return answer
