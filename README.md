### NB: If the instructions below are not clear, I attached video in this folder showing how to implement the.

## Type of chatbot:
### This a dictionary chatbot.

## About the chatbot:
### you can make request using the following keywords:
#### - Define
#### - Antonym
#### - Synonym
#### - Syllables
#### - Part of 
#### - Pronunciation
#### - Use in a sentence
#### - everything

### Here are examples of requests to make:
#### example1: define life,
#### example2: antonym of kind,
#### example3: synonym of happy,
#### example4: Syllables of entertainment,
#### example5: a wheel is a part of,
#### example6: Pronunciation of entertainment,
#### example7: Use careful in a sentence,
#### example7: Give me everything about lemon,

## Rest api endpoints:
### ~ /chat  method = ['get', 'post', 'delete']
#### You post requests and get responses. You can get all the messages with the chatbot including timestamps. AUTHORIZATION REQUIRED.

### ~ /login  method = ['post']
#### You can login and get token key in response.

### ~ /register  method = ['post']
#### You can register and get token key in response.

### ~ /logout  method = ['post']
#### You can logout and the token key gets removed. AUTHORIZATION REQUIRED.

### ~ /delete-account  method = ['delete']
#### You can delete your account. AUTHORIZATION REQUIRED.

## Interact with the rest api
#### You can either use the browser https://word-chatbot.onrender.com/doc or use curl. 
#### I suggest that you use the browser, it's very easy to use.

## Instructions for using the browser:
### url: https://word-chatbot.onrender.com/doc
### 1: Register / Login (You'll get the token key in response)
### 2: Copy the token key and press "Authorize" button, type Token and paste token key. E.g Token 43h5b4rf34tt434t
### 3. Now you're authorized and use /chat endpoint to send requests.
### 4. When you're done you can /logout or /delete-account

## Instructions for using curl:
### 1: Register an account using the code below. Replace values with your own.
#### curl -X POST -d username=test -d email=test@gmail.com -d password=Password@123 -d password2=Password@123 https://word-chatbot.onrender.com/register

### 2: Copy the token key you got as a response
### 3: You can post a request to the chatbot.
#### curl --location 'https://word-chatbot.onrender.com/chat' --header 'Authorization: Token c0b655d30d08af8ed6cf480d821173d47f6d94e7' --header 'Content-Type: application/json' --data '{"user_input": "Use beautiful in a sentence"}'

### 4: You can get all the chat messages.
#### curl --location 'https://word-chatbot.onrender.com/chat' --header 'Authorization: Token 53684366e1470bfb336f6bbd9433799ccb5fd53f'

### 5: You can delete all the messages
#### curl --location --request DELETE 'https://word-chatbot.onrender.com/chat' --header 'Authorization: Token c0b655d30d08af8ed6cf480d821173d47f6d94e7'

#### 6: You can logout
#### curl --location --request POST 'https://word-chatbot.onrender.com/logout' --header 'Authorization: Token f9e697c4216401c03098daa295fa86e0291b5c84'



