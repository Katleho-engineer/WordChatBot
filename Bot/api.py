import requests

# header for connecting to the api
headers = {
        "X-RapidAPI-Key": "f1ab364b9amsh47af4fe40162754p1f1b53jsne8e93ad1642d",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }


# returns everything about the word
def wordAPI_everything(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}"
    response = requests.get(url, headers=headers)

    return response.json()


# returns definition of the word
def wordAPI_define(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions"
    response = requests.get(url, headers=headers)

    return response.json()


# returns synonyms of the word
def wordAPI_synonyms(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/synonyms"
    response = requests.get(url, headers=headers)

    return response.json()


# returns antonyms of the word
def wordAPI_antonyms(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/antonyms"
    response = requests.get(url, headers=headers)

    return response.json()


# returns a way to pronounce a word
def wordAPI_pronunciation(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/pronunciation"
    response = requests.get(url, headers=headers)

    return response.json()


# returns syllables of a word
def wordAPI_syllables(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/syllables"
    response = requests.get(url, headers=headers)

    return response.json()


# returns examples of how to use the word in a sentence
def wordAPI_examples(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/examples"
    response = requests.get(url, headers=headers)

    return response.json()


# returns what the word forms part of.
def wordAPI_partOf(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/partOf"
    response = requests.get(url, headers=headers)

    return response.json()


