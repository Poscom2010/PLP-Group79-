# Crypto-Tom Chatbot: AI Wk 1 Specialization assignment.
# Step 1: Welcome Messages:Greeting and Personality

import time

print("Hello, welcome☺, iam Crypto Tom, your side pocket Crypto friend. ")
print("Ask me about crypto currency, and I can analyze the current crypto trends and give you the promising instruments so that you can trade with a bang 💸💰. ")

#Step 2:Adding the Crypto dataset
crypto_data = [
    {"name": "Bitcoin", "price_trend": "up", "energy_usage": "high", "project_viability": "strong"},
    {"name": "Ethereum", "price_trend": "up", "energy_usage": "medium", "project_viability": "strong"},
    {"name": "Dogecoin", "price_trend": "down", "energy_usage": "high", "project_viability": "weak"},
    {"name": "Cardano", "price_trend": "up", "energy_usage": "low", "project_viability": "medium"},
    {"name": "Solana", "price_trend": "down", "energy_usage": "medium", "project_viability": "medium"},
    {"name": "Polkadot", "price_trend": "up", "energy_usage": "low", "project_viability": "strong"},
    {"name": "Litecoin", "price_trend": "down", "energy_usage": "medium", "project_viability": "medium"},
    {"name": "Avalanche", "price_trend": "up", "energy_usage": "low", "project_viability": "medium"},
    {"name": "Ripple", "price_trend": "up", "energy_usage": "medium", "project_viability": "strong"},
    {"name": "Stellar", "price_trend": "down", "energy_usage": "low", "project_viability": "strong"},
    {"name": "Chainlink", "price_trend": "up", "energy_usage": "medium", "project_viability": "strong"},
    {"name": "VeChain", "price_trend": "up", "energy_usage": "low", "project_viability": "medium"},
    {"name": "NEO", "price_trend": "down", "energy_usage": "high", "project_viability": "weak"},
    {"name": "Algorand", "price_trend": "up", "energy_usage": "low", "project_viability": "strong"},
    {"name": "Tezos", "price_trend": "down", "energy_usage": "medium", "project_viability": "weak"},
    {"name": "Cosmos", "price_trend": "up", "energy_usage": "low", "project_viability": "medium"},
    {"name": "Hedera", "price_trend": "up", "energy_usage": "low", "project_viability": "strong"},
    {"name": "Zcash", "price_trend": "down", "energy_usage": "high", "project_viability": "medium"},
    {"name": "EOS", "price_trend": "down", "energy_usage": "medium", "project_viability": "weak"},
    {"name": "Trumpcoin", "price_trend": "up", "energy_usage": "high", "project_viability": "strong"}

]

# Ask User Input
user_name = input("What is your name: ").upper()
bold_name = f"\033[1m{user_name}\033[0m"
print(f"Welcome 👌{bold_name}👌, I'm-Crypto Tom!🤖 Its a pleasure to meet you. 🤝")

#Loop for continuity
while True:

    user_input = input("\nWhich crypto coin(s) would you like to dig into?...(Type Exit / quit): ").lower()
    if user_input in "exit" or user_input in "quit":
        print("Thank you for visiting Crypto Tom!...A bientot👋 ")
        break
    else:
        coins = user_input.split()

# Find Crypto in the data
    found = False
    for each_coin in coins:
        for crypto in crypto_data:
            bold_crypto_name = f"\033[1m{crypto['name']}\033[0m"
            if crypto["name"].lower() == each_coin.lower():
                found = True
                print(f"📊 Analyzing {bold_crypto_name} ......")
                #time.sleep(7)

                #if else logic
                if crypto["price_trend"] == "up" and crypto["energy_usage"] != "high" and crypto ["project_viability"] == "strong":
                    print(f"✅ This is a promising project!! The trend is going, energy usage is low and project viability is strong...good choice to consider ")
                elif crypto ["price_trend"] == "up" and crypto ["energy_usage"] in ["medium", "high"]:
                    print(f"Hmmm🤔 the {bold_crypto_name} project is doing ok,BUT please check the energy usage or project viability first")

                else:
                    print(f"As a friend, i would not recommend you to take a bite on the {bold_crypto_name}⛔!!⚡project buddie.Its either price is going down or the project is not strong")

    if not found:
        print(f"ooops! buddie, {bold_crypto_name} not found, please try a different one")



    if not found:
        print("ooops! buddie, i searched and could not find that project, could you please try a different one")'''
