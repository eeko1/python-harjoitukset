import math

leivi = float(input("Anna leiviskät."))
naula = float(input("Anna naulat."))
luoti = float(input("Anna luodit."))

luoti_grammoina = luoti * 13.3
naula_grammoina = naula * 32 * 13.3
leivi_grammoina = leivi * 20 * 32 * 13.3

gramma = luoti_grammoina + naula_grammoina + leivi_grammoina
kilot = math.floor(gramma // 1000)
gramma2 = gramma % 1000

print(f"Massa nykymittojen mukaan:")
print(f"{kilot}  kilogrammaa ja  {gramma2:.2f} grammaa.")

#kilot = math.floor(gramma // 1000)