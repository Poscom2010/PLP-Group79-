# Crypto-Tom Chatbot: AI Wk 1 Specialization assignment.
# Step 1: Welcome Messages:Greeting and Personality

import time
import sys

print("Hello, welcome☺, iam Crypto Tom, your side pocket Crypto friend. ")
time.sleep(2)

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
user_name = input("What is your name: ").title()
bold_name = f"\033[1m{user_name}\033[0m"
print(f"Welcome 👌{bold_name}👌, I'm-Crypto Tom!🤖 Its a pleasure to meet you. 🤝")
time.sleep(3)
print("Please NOTE💀, Cryptocurrency markets are highly volatile and involve significant risks.\nCrypto Tom is not a financial advisor and will not be liable to risks you incur. ")
time.sleep(2)

#Loop for continuity
while True:

    user_input = input("\nWhich crypto coin would you like to dig into?...(Type Exit / quit): ").strip().lower()
    if user_input in ["exit","quit"]:
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
                time.sleep(5)

            #if else logic
                if crypto["price_trend"] == "up" and crypto["energy_usage"] != "high" and crypto ["project_viability"] == "strong":
                    print(f"✅ {bold_crypto_name} is a promising project!! The trend is going, energy usage is low and project viability is strong...good choice to consider ")
                elif crypto ["price_trend"] == "up" and crypto ["energy_usage"] in ["medium", "high"]:
                    print(f"Hmmm🤔 the {bold_crypto_name} project is doing ok,BUT please check the energy usage or project viability first")

                else:
                    print(f"As a friend, i would not recommend you to take a bite on the {bold_crypto_name}⛔!!⚡project buddie.Its either price is going down or the project is not strong")
    if not found:
        print("ooops! buddie, i searched and could not find that project, Please try a different one")
