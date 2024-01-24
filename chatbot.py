import random
def respond(user_input):
    rules = {
        "Hai":["Hey there!","Hai! How can i assist you?"],
        "How do you do?":["I am doing well.Thanks for asking","I am great thanks for asking"],
        "Tell me about todays weather condition":["Its currently rainy in Las vegas","There may be a light shower tonight"],
        "Suggest me a car brand":["Tata","honda","bmw","mercedes","Suzuki"],
        "Thank you":["Your always welcome!","See you tommorow bai"]
    }
    for pattern, responses in rules.items():
        if pattern in user_input:
            return random.choice(responses)
    return "I am not sure about this.Could you make change in question?"
while True:
        user_input = input("Me: ")
        response = respond(user_input)
        print("ChatBot: ", response)