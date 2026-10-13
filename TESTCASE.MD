# Test Case Documentation

## Ayurvedic Classification as a Rule-Based Expert System

**Student:** Shubham Pandey\
**Course:** T.Y.B.Sc. Computer Science \| Semester V\
**Project:** IKS Project \| 2026--27\
**Language:** Python 3\
**File Tested:** `expert_system.py`\
**Interface:** Command line\
**Libraries:** None (standard Python only)

------------------------------------------------------------------------

## 1. Objective

To verify that the expert system:

-   Gives the correct Prakriti for single-dosha, dual-dosha, and
    balanced inputs.
-   Handles extreme scores such as `8 / 0 / 0` correctly.
-   Applies classification rules C1, C2, and C3 at their boundaries.
-   Rejects invalid input and asks the user to try again.

## 2. How Expected Results Are Decided

Each of the eight answers adds one point to a dosha. The total score is
therefore 8. The dosha scores are sorted into top, middle, and low
values, and the first matching classification rule is applied.

  Rule   Condition                              Result
  ------ -------------------------------------- -------------------------------------
  C1     `top - mid >= 2`                       Single dosha (Ekadoshaja)
  C2     `top - mid < 2` and `top - low >= 2`   Dual dosha (Dvandvaja)
  C3     `top - low <= 1`                       Balanced (Sannipataja / Tridoshaja)

**Input order:** frame, skin, appetite, sleep, climate, temperament,
activity, stress.

## 3. Summary of Results

  ------------------------------------------------------------------------------
  ID          Category     Scores (V / P Expected Result Rule        Status
                                    / K)                             
  ----------- ----------- -------------- --------------- ----------- -----------
  T1          Single           7 / 1 / 0 Vata Prakriti   C1          Pass
              dosha                      (Ekadoshaja)                

  T2          Single           1 / 7 / 0 Pitta Prakriti  C1          Pass
              dosha                      (Ekadoshaja)                

  T3          Dual dosha       0 / 4 / 4 Pitta-Kapha     C2          Pass
                                         Prakriti                    
                                         (Dvandvaja)                 

  T4          Balanced         3 / 3 / 2 Sama Prakriti   C3          Pass
                                         (Sannipataja)               

  T5          Extreme:         8 / 0 / 0 Vata Prakriti   C1          Pass
              all Vata                   (Ekadoshaja)                

  T6          Extreme:         0 / 0 / 8 Kapha Prakriti  C1          Pass
              all Kapha                  (Ekadoshaja)                

  T7          Boundary of      5 / 3 / 0 Vata Prakriti   C1          Pass
              C1                         (Ekadoshaja)                

  T8          Boundary of      4 / 3 / 1 Vata-Pitta      C2          Pass
              C2                         Prakriti                    
                                         (Dvandvaja)                 

  T9          Tie at top       4 / 4 / 0 Vata-Pitta      C2          Pass
                                         Prakriti                    
                                         (Dvandvaja)                 

  T10         Boundary of      3 / 3 / 2 Sama Prakriti   C3          Pass
              C3                         (Sannipataja)               

  T11         Invalid                N/A Reject input    ---         Pass
              input                      and ask again               
  ------------------------------------------------------------------------------

**Final result:** 11 out of 11 test cases passed (100%), as documented
for this project.

## 4. Detailed Test Cases

### T1: Single Dosha --- Vata

-   **Purpose:** Check classification when Vata is much higher than the
    other doshas.
-   **Input:**
    `thin, dry, irregular, light, dislikes_cold, quick_anxious, restless, anger`
-   **Scores:** Vata 7, Pitta 1, Kapha 0
-   **Check:** `top - mid = 7 - 1 = 6`, which is at least 2, so C1
    applies.
-   **Expected result:** Vata Prakriti (Ekadoshaja)
-   **Status:** Pass

### T2: Single Dosha --- Pitta

-   **Purpose:** Check classification when Pitta is much higher than the
    other doshas.
-   **Input:**
    `medium, warm, strong, moderate, dislikes_heat, sharp_irritable, purposeful, worry`
-   **Scores:** Vata 1, Pitta 7, Kapha 0
-   **Check:** `top - mid = 7 - 1 = 6`, which is at least 2, so C1
    applies.
-   **Expected result:** Pitta Prakriti (Ekadoshaja)
-   **Status:** Pass

### T3: Dual Dosha --- Pitta-Kapha

-   **Purpose:** Check classification when Pitta and Kapha have equal
    scores.
-   **Input:**
    `large, oily, strong, moderate, dislikes_damp, sharp_irritable, slow_steady, anger`
-   **Scores:** Vata 0, Pitta 4, Kapha 4
-   **Check:** `top - mid = 0` (less than 2) and `top - low = 4` (at
    least 2), so C2 applies.
-   **Expected result:** Pitta-Kapha Prakriti (Dvandvaja)
-   **Status:** Pass

### T4: Balanced --- Sama

-   **Purpose:** Check classification when all three doshas have similar
    scores.
-   **Input:**
    `thin, warm, slow, light, dislikes_heat, calm_steady, restless, anger`
-   **Scores:** Vata 3, Pitta 3, Kapha 2
-   **Check:** `top - low = 3 - 2 = 1`, which is at most 1, so C3
    applies.
-   **Expected result:** Sama Prakriti (Sannipataja / Tridoshaja)
-   **Status:** Pass

### T5: Extreme Score --- All Vata

-   **Purpose:** Test the maximum possible score for Vata.
-   **Input:**
    `thin, dry, irregular, light, dislikes_cold, quick_anxious, restless, worry`
-   **Scores:** Vata 8, Pitta 0, Kapha 0
-   **Check:** The top score exceeds the middle score by 8, so C1
    applies.
-   **Expected result:** Vata Prakriti (Ekadoshaja)
-   **Status:** Pass

### T6: Extreme Score --- All Kapha

-   **Purpose:** Test the maximum possible score for Kapha.
-   **Input:**
    `large, oily, slow, deep, dislikes_damp, calm_steady, slow_steady, withdrawal`
-   **Scores:** Vata 0, Pitta 0, Kapha 8
-   **Check:** The top score exceeds the middle score by 8, so C1
    applies.
-   **Expected result:** Kapha Prakriti (Ekadoshaja)
-   **Status:** Pass

### T7: Boundary of C1 --- Gap Exactly 2

-   **Purpose:** Test the smallest score gap that still gives a single
    dosha.
-   **Input:**
    `thin, dry, irregular, light, dislikes_cold, sharp_irritable, purposeful, anger`
-   **Scores:** Vata 5, Pitta 3, Kapha 0
-   **Check:** `top - mid = 5 - 3 = 2`, so C1 applies.
-   **Expected result:** Vata Prakriti (Ekadoshaja)
-   **Status:** Pass

### T8: Boundary of C2 --- Gap of 1

-   **Purpose:** Check that a top-to-middle gap of 1 gives a dual-dosha
    result.
-   **Input:**
    `thin, dry, irregular, light, dislikes_heat, sharp_irritable, purposeful, withdrawal`
-   **Scores:** Vata 4, Pitta 3, Kapha 1
-   **Check:** `top - mid = 1` (less than 2) and `top - low = 3` (at
    least 2), so C2 applies.
-   **Expected result:** Vata-Pitta Prakriti (Dvandvaja)
-   **Status:** Pass

### T9: Tie at the Top

-   **Purpose:** Check classification when two doshas share the highest
    score.
-   **Input:**
    `thin, dry, irregular, light, dislikes_heat, sharp_irritable, purposeful, anger`
-   **Scores:** Vata 4, Pitta 4, Kapha 0
-   **Check:** `top - mid = 0` and `top - low = 4`, so C2 applies.
-   **Expected result:** Vata-Pitta Prakriti (Dvandvaja)
-   **Status:** Pass

### T10: Boundary of C3 --- Top Minus Low Equals 1

-   **Purpose:** Test the largest score difference that still counts as
    balanced.
-   **Input:**
    `thin, dry, irregular, moderate, dislikes_heat, sharp_irritable, slow_steady, withdrawal`
-   **Scores:** Vata 3, Pitta 3, Kapha 2
-   **Check:** `top - low = 3 - 2 = 1`, so C3 applies.
-   **Expected result:** Sama Prakriti (Sannipataja / Tridoshaja)
-   **Status:** Pass

### T11: Invalid Input Handling

-   **Purpose:** Confirm that invalid answers do not crash the program
    and are not accepted.
-   **Input:** `0`, `4`, `abc`, or a blank answer at any question.
-   **Check:** Only valid choices `1`, `2`, or `3` should be accepted by
    `ask_user()`.
-   **Expected result:** The program displays
    `Invalid input, try again.` and asks the same question again.
-   **Status:** Pass

## 5. Sample Output (T3)

``` text
----- RESULT -----
Vata   score: 0
Pitta  score: 4
Kapha  score: 4
Prakriti : Pitta-Kapha Prakriti (Dvandvaja)

----- EXPLANATION (rules fired) -----
R03: IF frame = large THEN Kapha +1
R06: IF skin = oily THEN Kapha +1
R08: IF appetite = strong THEN Pitta +1
R11: IF sleep = moderate THEN Pitta +1
R15: IF climate = dislikes_damp THEN Kapha +1
R17: IF temperament = sharp_irritable THEN Pitta +1
R21: IF activity = slow_steady THEN Kapha +1
R23: IF stress = anger THEN Pitta +1
C2: classification rule fired -> Pitta-Kapha Prakriti (Dvandvaja)
```

## 6. How to Run the Tests

1.  Open a terminal or CMD in the project folder.

2.  Run:

    ``` bash
    python expert_system.py
    ```

3.  Enter the choices for the eight questions. Use `1` for the first
    option, `2` for the second option, and `3` for the third option.

## 7. Test Coverage

  Area                    Covered by
  ----------------------- --------------------
  Rule C1: single dosha   T1, T2, T5, T6, T7
  Rule C2: dual dosha     T3, T8, T9
  Rule C3: balanced       T4, T10
  Extreme scores          T5, T6
  Boundary values         T7, T8, T10
  Tie handling            T9
  Input validation        T11

## 8. Conclusion

The documented test cases cover single-dosha, dual-dosha, and balanced
Prakriti classification, extreme scores, classification boundaries,
ties, and invalid input handling. The recorded result is 11 out of 11
tests passed.

**Prepared by:** Shubham Pandey\
**Course:** T.Y.B.Sc. Computer Science, Semester V\
**Guide:** Asst. Prof. Sini V.

> Educational project only. This system is not medical advice.
