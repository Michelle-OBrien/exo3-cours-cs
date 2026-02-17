import random

def ask_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("➡️  Entre un nombre entier.")

def pick_difficulty():
    print("\nChoisis une difficulté :")
    print("1) Facile   (1–50, 10 essais)")
    print("2) Normal   (1–100, 8 essais)")
    print("3) Difficile(1–500, 9 essais)")
    d = ask_int("Ton choix (1/2/3) : ")

    if d == 1:
        return 50, 10
    if d == 3:
        return 500, 9
    return 100, 8  # défaut

def play_round(max_value: int, attempts: int) -> int:
    target = random.randint(1, max_value)
    low, high = 1, max_value

    print(f"\n🎯 Je pense à un nombre entre 1 et {max_value}.")
    print(f"Tu as {attempts} essais. Bonne chance !")

    for i in range(1, attempts + 1):
        guess = ask_int(f"Essai {i}/{attempts} (entre {low} et {high}) : ")

        if guess < low or guess > high:
            print("⚠️  Hors de la plage indiquée. Ça compte quand même comme un essai.")
        if guess == target:
            print(f"✅ Bravo ! C’était {target}.")
            # score = points restants
            return attempts - i + 1

        if guess < target:
            print("📈 C’est plus !")
            low = max(low, guess + 1)
        else:
            print("📉 C’est moins !")
            high = min(high, guess - 1)

        if low > high:
            # cas extrême si l'utilisateur a fait n'importe quoi
            low, high = 1, max_value

    print(f"❌ Perdu. Le nombre était {target}.")
    return 0

def main():
    print("🎲 Bienvenue dans Le Juste Prix (version terminal)")

    score = 0
    rounds = 0

    while True:
        max_value, attempts = pick_difficulty()
        rounds += 1
        score += play_round(max_value, attempts)

        print(f"\n⭐ Score total : {score} (manche(s) jouée(s) : {rounds})")
        again = input("Rejouer ? (o/n) : ").strip().lower()
        if again not in ("o", "oui", "y", "yes"):
            break

    print("\n👋 Merci d'avoir joué !")

if __name__ == "__main__":
    main()
