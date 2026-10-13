"""
Ayurvedic Classification as a Rule-Based Expert System
Prakriti classification using forward chaining.
Educational project only - not a medical diagnosis tool.
"""

DOSHAS = ["Vata", "Pitta", "Kapha"]

# Knowledge base: attributes and options (Vata, Pitta, Kapha)
ATTRIBUTES = {
    "frame": ("Body frame", [
        ("thin", "Thin and light"),
        ("medium", "Medium and muscular"),
        ("large", "Large and heavy"),
    ]),
    "skin": ("Skin type", [
        ("dry", "Dry and rough"),
        ("warm", "Warm, sensitive, prone to redness"),
        ("oily", "Oily, smooth and soft"),
    ]),
    "appetite": ("Appetite and digestion", [
        ("irregular", "Irregular appetite"),
        ("strong", "Strong appetite, quick digestion"),
        ("slow", "Low appetite, slow digestion"),
    ]),
    "sleep": ("Sleep pattern", [
        ("light", "Light, easily disturbed"),
        ("moderate", "Moderate and sound"),
        ("deep", "Deep and long"),
    ]),
    "climate": ("Climate dislike", [
        ("dislikes_cold", "Dislikes cold and wind"),
        ("dislikes_heat", "Dislikes heat and sun"),
        ("dislikes_damp", "Dislikes damp, cool weather"),
    ]),
    "temperament": ("Temperament", [
        ("quick_anxious", "Quick, enthusiastic, anxious"),
        ("sharp_irritable", "Sharp, focused, irritable"),
        ("calm_steady", "Calm, steady, forgiving"),
    ]),
    "activity": ("Activity level", [
        ("restless", "Restless, always moving"),
        ("purposeful", "Purposeful and goal oriented"),
        ("slow_steady", "Slow, steady, enduring"),
    ]),
    "stress": ("Reaction to stress", [
        ("worry", "Worry and fear"),
        ("anger", "Anger and frustration"),
        ("withdrawal", "Withdrawal and silence"),
    ]),
}

ADVICE = {
    "Vata": (
        "Prefer warm, cooked, moist foods; keep a regular routine; "
        "get enough rest; avoid cold, dry and very irregular habits."
    ),
    "Pitta": (
        "Prefer cooling, mildly sweet and bitter foods; avoid excess "
        "spicy, fried and sour food; avoid overheating and overwork."
    ),
    "Kapha": (
        "Prefer light, warm, spiced food; take regular vigorous "
        "exercise; avoid heavy, oily, sweet food and daytime sleep."
    ),
}


def build_rules():
    """Create scoring rules: IF attribute=value THEN dosha score +1."""
    rules = []
    number = 1
    for attribute, (_, options) in ATTRIBUTES.items():
        for index, (value, _) in enumerate(options):
            rules.append({
                "id": "R%02d" % number,
                "attr": attribute,
                "val": value,
                "dosha": DOSHAS[index],
            })
            number += 1
    return rules


RULES = build_rules()


def infer(facts):
    """Apply matching rules and classify the Prakriti."""
    score = {dosha: 0 for dosha in DOSHAS}
    trace = []

    # Apply scoring rules
    for rule in RULES:
        if facts.get(rule["attr"]) == rule["val"]:
            score[rule["dosha"]] += 1
            trace.append(
                "{}: IF {} = {} THEN {} +1".format(
                    rule["id"], rule["attr"], rule["val"], rule["dosha"]
                )
            )

    # Rank doshas by score
    ranked = sorted(DOSHAS, key=lambda dosha: -score[dosha])
    top, mid, low = (score[dosha] for dosha in ranked)

    # Classification rules
    if top - mid >= 2:
        rule = "C1"
        result = "{} Prakriti (Ekadoshaja)".format(ranked[0])
        advice = ADVICE[ranked[0]]
    elif top - low <= 1:
        rule = "C3"
        result = "Sama Prakriti (Sannipataja / Tridoshaja)"
        advice = "Maintain balance of all three doshas with a varied diet."
    else:
        rule = "C2"
        result = "{}-{} Prakriti (Dvandvaja)".format(ranked[0], ranked[1])
        advice = ADVICE[ranked[0]] + " Also: " + ADVICE[ranked[1]]

    trace.append("Classification rule fired -> {}: {}".format(rule, result))
    return {"score": score, "result": result, "advice": advice, "trace": trace}


def ask_user():
    """Ask eight questions and store the selected answers."""
    facts = {}
    for attribute, (title, options) in ATTRIBUTES.items():
        print("\n{}".format(title))
        for number, (_, description) in enumerate(options, 1):
            print("  {}. {}".format(number, description))

        while True:
            choice = input("Enter choice (1-3): ").strip()
            if choice in ("1", "2", "3"):
                facts[attribute] = options[int(choice) - 1][0]
                break
            print("Invalid input, try again.")
    return facts


def show(output):
    """Display scores, result, advice and explanation."""
    print("\n--------------- RESULT ---------------")
    for dosha in DOSHAS:
        print("{} score : {}".format(dosha, output["score"][dosha]))
    print("Prakriti    : {}".format(output["result"]))
    print("Advice      : {}".format(output["advice"]))
    print("\n----- EXPLANATION (rules fired) -----")
    for line in output["trace"]:
        print(line)


if __name__ == "__main__":
    print("AYURVEDIC PRAKRITI EXPERT SYSTEM")
    show(infer(ask_user()))
    print("\nNote: Educational use only; consult a qualified Vaidya for health concerns.")
