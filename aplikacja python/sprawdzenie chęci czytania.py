def is_privacy_policy_accepted():
    try:
        with open("privacy_policy.txt", "r", encoding="utf-8") as policy_file:
            lines = policy_file.readlines()
            for line in lines:
                print(line, end=" ")

            choice = input("\nCzy zgadzasz się na politykę prywatności? (T/N): ")
            return choice.upper() == 'T'
    except FileNotFoundError:
        print("Nie można wczytać polityki prywatności.")
        return False

privacy_policy_accepted = is_privacy_policy_accepted()

if not privacy_policy_accepted:
    print(" Gratulujemy uważności, powyższy regulamin negatywnie wpływa na dane osobowe użytkownika.")
else:
    print(" Radzimy ponowne przeczytanie regulaminu, wpływa on negatywnie na dane i prywatność użytkownika")
input("")
while True:
    pass
