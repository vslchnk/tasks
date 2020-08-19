import secrets

x = list(range(1, 11))
secrets.SystemRandom().shuffle(x)

print(*x)
