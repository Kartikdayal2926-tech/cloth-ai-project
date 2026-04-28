import random

def get_recommendation(gender, occasion, color, season):

    outfits = {
        "male": {
            "casual": [
                f"{color} t-shirt with ripped jeans",
                f"{color} hoodie with joggers"
            ],
            "party": [
                f"{color} blazer with black jeans",
                f"{color} shirt with slim-fit trousers"
            ],
            "formal": [
                f"{color} suit with tie",
                f"{color} formal shirt with trousers"
            ]
        },
        "female": {
            "casual": [
                f"{color} top with denim skirt",
                f"{color} oversized t-shirt with shorts"
            ],
            "party": [
                f"{color} evening gown",
                f"{color} stylish dress with heels"
            ],
            "formal": [
                f"{color} blazer with pencil skirt",
                f"{color} formal kurti with pants"
            ]
        }
    }

    try:
        return random.choice(outfits[gender][occasion])
    except:
        return f"{color} stylish outfit for {season}"