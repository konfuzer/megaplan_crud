import requests
from config import HOST, TOKEN, FIELD_NAME

def get_deal(deal_id):
    url = f"{HOST}/api/v3/deal/{deal_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()

def update_deal_field(deal_id, values):
    """
    values: список моделей, например ["A1", "XC60"]
    сохраняем как строку: "Audi:A1, Volvo:XC60"
    """
    brand_map = {
        "A1": "Audi", "A3": "Audi", "Q5": "Audi", "Q7": "Audi",
        "XC60": "Volvo", "XC90": "Volvo", "V40": "Volvo", "C30": "Volvo",
        "Vesta": "Lada", "Granta": "Lada", "Aura": "Lada", "Priora": "Lada"
    }

    result = []
    for model in values:
        brand = brand_map.get(model, "Unknown")
        result.append(f"{brand}:{model}")

    value_str = ", ".join(result)

    url = f"{HOST}/api/v3/deal/{deal_id}"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "deal": {
            FIELD_NAME: value_str
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()
