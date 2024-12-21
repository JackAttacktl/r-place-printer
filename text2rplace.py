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
ffaff
fafaf
afffa
aaaaa
afffa
afffa
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
aaaf
affa
affa
affa
affa
aaaf
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
faaaaf
affffa
affffa
affffa
affffa
faaaaf
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
affa
faaf
""",
    "T": """
aaaaa
ffaff
ffaff
ffaff
ffaff
ffaff
""",
    "U": """
afffa
afffa
afffa
afffa
afffa
faaaf
""",
    "V": """
fafffaf
fafffaf
ffafaff
ffafaff
fffafff
fffafff
""",
    "W": """
afffa
afffa
afffa
afafa
aafaa
afffa
""",
    "X": """
affffa
affffa
faaaaf
faaaaf
affffa
affffa
""",
    "Y": """
afffa
afffa
fafaf
ffaff
ffaff
ffaff
""",
    "Z": """
aaaa
fffa
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
fffaf
fffaf
ffaff
ffaff
fafff
fafff
""",
    ".": """
ffff
ffff
ffff
ffff
faaf
faaf
""",
    ",": """
ffff
ffff
ffff
ffff
faaf
faaf
ffaf
"""
}

text = "A,."

max_line_count = 0

for l in text:
    letter_codes = fonts[l][1:][:-1]
    code_lines = letter_codes.split('\n')
    max_line_count = max(max_line_count,len(code_lines))

fill_letter = "f"

lines = []
for l in text:
    letter_codes = fonts[l][1:][:-1]
    code_lines = letter_codes.split('\n')
    if (len(lines) < len(code_lines)):
        for _ in range(len(code_lines) - len(lines)):
            if (len(lines) > 0):
                lines.append(fill_letter*len(lines[len(lines)-1]))
            else:
                lines.append('')

    max_line_length = 0
    for i,line in enumerate(lines):
        if (len(code_lines) > i):
            lines[i] = line + code_lines[i] + fill_letter
            if (len(code_lines[i]) > max_line_length):
                max_line_length = len(code_lines[i])
        else:
            lines[i] = line + (max_line_length*fill_letter) + fill_letter

final_text = ''
for line in lines:
    final_text += line + '\n'

print("Height: " + str(max_line_count))
print("Width: " + str(len(lines[0])))
print(final_text)
