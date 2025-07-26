"""
Obfuscation Types Used:

Manual Obfuscation:
- Function: factorial → process_D34fX
- Variable names changed: n → input_E99qP, result → tempVal_Bb
- Loop var renamed to Zz

Automatic Obfuscation (Simulated):
- Compressed to one line using inline operations
- Function and variable names minimized
- Reduces readability and reversibility

Goal:
- Demonstrates how obfuscation hides program intent
- Useful for protecting code logic from reverse engineering
"""

import random

# ============================
# Part 1: ZKP – Ali Baba Cave Simulation (Modified Style)
# ============================

def zkp_simulation(trials, knows_secret):
    """
    Simulates the Ali Baba Cave ZKP protocol.
    Parameters:
        trials (int): Number of protocol rounds
        knows_secret (bool): Whether prover knows the secret (password)
    Returns:
        success_rate (float): Prover's success percentage
    """
    correct_guesses = 0
    for attempt in range(trials):
        entered = random.choice(['left', 'right'])
        challenge = random.choice(['left', 'right'])

        if knows_secret:
            verified = True
        else:
            verified = entered == challenge  # attacker guesses correctly

        if verified:
            correct_guesses += 1

    probability = correct_guesses / trials
    print(f"\nZKP Simulation Results:")
    print(f"Successes: {correct_guesses}/{trials} ({probability*100:.2f}%)")
    return probability

print(">>> Honest Prover (Knows Password):")
zkp_simulation(trials=20, knows_secret=True)

print("\n>>> Malicious Prover (Does NOT Know Password):")
zkp_simulation(trials=20, knows_secret=False)

# ============================
# Part 2: Code Obfuscation Challenge – Factorial Function
# ============================

# --- Original Version ---
def factorial(n):
    """
    Calculates the factorial of a number using a loop.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("\nOriginal Factorial (n=5):", factorial(5))

# --- Manually Obfuscated Version ---
def process_D34fX(input_E99qP):
    """
    Obfuscated function with renamed identifiers.
    """
    tempVal_Bb = 1
    for Zz in range(2, input_E99qP + 1):
        tempVal_Bb *= Zz
    return tempVal_Bb

print("Manually Obfuscated Factorial (n=5):", process_D34fX(5))

# --- Automatically Obfuscated (Simulated) Version ---
def g(u):v=1;[v:=v*i for i in range(2,u+1)];return v
print("Auto-Obfuscated Simulation (n=5):", g(5))

