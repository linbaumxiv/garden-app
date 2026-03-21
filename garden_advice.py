def get_gardening_advice(season, plant_type):
    advice_data = {
        "seasons": {
            "summer": "Water your plants regularly and provide some shade.",
            "winter": "Protect your plants from frost with covers."
        },
        "types": {
            "flower": "Use fertiliser to encourage blooms.",
            "vegetable": "Keep an eye out for pests!"
        },
        # Add this new dictionary section
        "recommendations": {
            "summer": "Tomatoes, Marigolds, and Sunflowers",
            "winter": "Kale, Carrots, and Pansies"
        }
    }

    # Fetch advice and add recommendation logic
    season_key = season.lower()
    season_msg = advice_data["seasons"].get(season_key, "No specific advice for this season.")
    type_msg = advice_data["types"].get(plant_type.lower(), "No specific advice for this plant type.")
    rec_msg = advice_data["recommendations"].get(season_key, "general hardy plants")

    return f"{season_msg}\n{type_msg}\nRecommended for {season}: {rec_msg}"