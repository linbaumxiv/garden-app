# gardening_advice.py

def get_gardening_advice(season, plant_type):
    # Store advice in a dictionary for easy maintenance
    advice_data = {
        "seasons": {
            "summer": "Water your plants regularly and provide some shade.",
            "winter": "Protect your plants from frost with covers."
        },
        "types": {
            "flower": "Use fertiliser to encourage blooms.",
            "vegetable": "Keep an eye out for pests!"
        }
    }

    # Fetch advice with fallback defaults
    season_msg = advice_data["seasons"].get(season.lower(), "No specific advice for this season.")
    type_msg = advice_data["types"].get(plant_type.lower(), "No specific advice for this plant type.")
    
    return f"{season_msg}\n{type_msg}"

def main():
    # Replace hardcoded values with user input
    user_season = input("Enter the current season: ")
    user_plant = input("Enter the plant type (flower/vegetable): ")
    
    result = get_gardening_advice(user_season, user_plant)
    print(f"\n--- Your Gardening Advice ---\n{result}")

if __name__ == "__main__":
    main()