
import re


def to_unicode_superscript(n: int) -> str:
    result = str()
    for c in str(n):
        result += {
            "1": "¹",
            "2": "²",
            "3": "³",
            "4": "⁴",
            "5": "⁵",
            "6": "⁶",
            "7": "⁷",
            "8": "⁸",
            "9": "⁹",
            "0": "⁰"
        }[c]
    return result

def beautify_equation(equation: str) -> str:
    # Because people can't be bothered to put freaking spaces between operators so that it looks nice
    for operator in '+×*=-/<>≥≤≠':
        equation = equation.replace(f" {operator} ", operator) # This is required to prevent double spaces when spaces are already there
        equation = equation.replace(operator, f" {operator} ")
    return equation

def laplace(equation: str, conditions_initialles_nulles = True) -> str:
    immédiat = []
    for term in beautify_equation(equation).split():
        if (match := re.match(r"(?u)(\w(?:[_\w]+)?)('*)\(t\)", term)):
            la_vie = match[1]
            derivation_count = len(match[2])
            oui_bon = ""
            if derivation_count:
                oui_bon = "p"
            if derivation_count >= 2:
                oui_bon += to_unicode_superscript(derivation_count) + " "
            on_va_pas_se_compliquer = "ε" if la_vie[0] == "ε" else la_vie[0].upper()
            immédiat += [oui_bon + on_va_pas_se_compliquer + la_vie[1:] + "(p)"]
        else:
            immédiat += [term]
    return ' '.join(immédiat)
        

def on_va_passer_en_laplace():
    equation = input("Équation: ")
    conditions_initialles_nulles = input("Conditions initiales nulles? ").lower().strip() != "non"
    if conditions_initialles_nulles:
        print("<Couprie> Alors oui booooh, on va passer en Laplace")
    else:
        print("<Couprie> Alors oui bon, en SI on se complique pas la vie hein, les conditions initiales sont nulles")
        print("<Python> M-M-Mais")
        print(">>> conditions_initialles_nulles = True")
    print(f"{beautify_equation(equation)} ···𝓛··> {laplace(equation)}")

while True:
    on_va_passer_en_laplace()
