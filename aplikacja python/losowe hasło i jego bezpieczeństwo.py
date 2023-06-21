import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    # Lista warunków oceny bezpieczeństwa hasła
    conditions = [
        lambda p: any(c.islower() for c in p),  # Mała litera
        lambda p: any(c.isupper() for c in p),  # Duża litera
        lambda p: any(c.isdigit() for c in p),  # Cyfra
        lambda p: any(c in string.punctuation for c in p),  # Znak specjalny
        lambda p: len(p) >= 8  # Minimalna długość
    ]

    # Ocena bezpieczeństwa hasła
    strength = sum(condition(password) for condition in conditions)
    return strength

length = int(input("Podaj długość hasła: "))
password = generate_password(length)
strength = check_password_strength(password)

print("Wygenerowane hasło:", password)
print("Ocena bezpieczeństwa:", strength, "na 5")

print("")
while True:
    pass
