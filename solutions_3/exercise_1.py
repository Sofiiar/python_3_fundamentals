s = 'FfEeDdCcBbAa'
uppercase_letters = ''.join(sorted([char for char in s if char.isupper()]))
lowercase_letters = ''.join(sorted([char for char in s if char.islower()]))

print("UPPERCASE: ", uppercase_letters)
print("lowercase: ", lowercase_letters)
