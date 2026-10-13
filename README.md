# Ayurvedic Classification as a Rule-Based Expert System

## Project Overview
This is a simple Python 3 project that classifies a user's Ayurvedic Prakriti using a rule-based expert system and forward chaining.

The program asks eight questions about:
- Body frame
- Skin type
- Appetite and digestion
- Sleep pattern
- Climate dislike
- Temperament
- Activity level
- Reaction to stress

It scores Vata, Pitta, and Kapha, then displays a Prakriti classification, general lifestyle guidance, and the rules used to reach the result.

## Requirements
- Python 3
- No external Python libraries are required.

## How to Run
1. Download or copy `expert_system.py`.
2. Open Command Prompt or a terminal in the folder containing the file.
3. Run:

   ```bash
   python expert_system.py
   ```

4. Answer each question by entering `1`, `2`, or `3`.

If `python` is not recognized, try:

```bash
py expert_system.py
```

## How It Works
1. The program collects answers to eight questions.
2. Each answer matches a scoring rule and adds one point to Vata, Pitta, or Kapha.
3. The program applies classification rules to select a Prakriti type.
4. It displays the scores, result, general advice, and fired rules.

## Main Files
- `expert_system.py` — the main Python program.
- `README.md` — project information and run instructions.

## Important Disclaimer
This project is for academic and educational purposes only. It is not a medical device and does not diagnose or treat diseases. Consult a qualified healthcare professional for health concerns.
