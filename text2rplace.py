import b64coder

fonts = {
    " ": """
fff
fff
fff
fff
fff
fff
""",
    "A": """
faaf
affa
aaaa
affa
affa
affa
""",
    "B": """
aaaf
affa
aaaf
aaaf
affa
aaaf
""",
    "C": """
faaa
afff
afff
afff
afff
faaa
""",
    "D": """
aaff
afaf
affa
affa
afaf
aaff
""",
    "E": """
aaaa
afff
aaaa
afff
afff
aaaa
""",
    "F": """
aaaa
afff
afff
aaaa
afff
afff
""",
    "G": """
aaaa
afff
afaa
affa
affa
aaaa
""",
    "H": """
affa
affa
aaaa
affa
affa
affa
""",
    "I": """
aaaa
faff
faff
faff
faff
aaaa
""",
    "J": """
aaaa
ffaf
ffaf
ffaf
afaf
aaaf
""",
    "K": """
affa
afaf
aaff
aaff
afaf
affa
""",
    "L": """
afff
afff
afff
afff
afff
aaaa
""",
    "M": """
affa
aaaa
affa
affa
affa
affa
""",
    "N": """
affa
aafa
afaa
affa
affa
affa
""",
    "O": """
faaf
affa
affa
affa
affa
faaf
""",
    "P": """
aaaa
affa
aaaa
afff
afff
afff
""",
    "Q": """
faaf
affa
affa
faaf
ffaf
fffa
""",
    "R": """
aaaf
affa
aaaf
afaf
affa
affa
""",
    "S": """
faaf
affa
faff
ffaf
fffa
faaf
""",
    "T": """
aaaa
faff
faff
faff
faff
faff
""",
    "U": """
affa
affa
affa
affa
affa
faaf
""",
    "V": """
affa
affa
affa
affa
faaf
faaf
""",
    "W": """
affa
affa
affa
affa
aaaa
affa
""",
    "X": """
affa
affa
faaf
faaf
affa
affa
""",
    "Y": """
affa
affa
affa
faaf
faaf
faaf
""",
    "Z": """
aaaa
ffaf
ffaf
faff
afff
aaaa
""",
    ":": """
ffff
faaf
faaf
ffff
faaf
faaf
""",
    "/": """
ffff
fffa
ffaf
faff
afff
ffff
""",
    ".": """
ffff
ffff
ffff
ffff
faaf
faaf
"""
}

line_count = 6

text = "HTTPS://NEEDCOOLERSHOES.COM"

fill_letter = "f"

lines = ['' for i in range(line_count)]
for l in text:
    letter_codes = fonts[l][1:][:-1]
    code_lines = letter_codes.split('\n')
    for i,line in enumerate(lines):
        lines[i] = line + code_lines[i] + fill_letter

final_text = ''
for line in lines:
    final_text += line + '\n'

print("Height: " + str(line_count))
print("Width: " + str(len(lines[0])))
print(final_text)
