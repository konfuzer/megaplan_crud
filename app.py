from flask import Flask, render_template, request, redirect
from config import DEAL_ID, FIELD_NAME
from megaplan_api import get_deal, update_deal_field

app = Flask(__name__)

OPTIONS = {
    "Audi": ["A1", "A3", "Q5", "Q7"],
    "Volvo": ["XC60", "XC90", "V40", "C30"],
    "Lada": ["Vesta", "Granta", "Aura", "Priora"]
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected = request.form.getlist("models")
        update_deal_field(DEAL_ID, selected)
        return redirect("/")

    deal_data = get_deal(DEAL_ID)
    print("===== API RESPONSE =====")
    print(deal_data)
    print("========================")

    raw_value = deal_data["data"].get(FIELD_NAME, "")
    # Извлекаем только модель из строки "Audi:A1"
    current_values = [part.split(":")[1].strip() for part in raw_value.split(",") if ":" in part]

    return render_template("form.html", options=OPTIONS, current=current_values)

if __name__ == "__main__":
    app.run(debug=True)
