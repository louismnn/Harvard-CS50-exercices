import re

inpt = input("camelCase: ")

def main(input_str):
    result = re.sub(r'(?<!^)([A-Z])', r'_\1', input_str)
    return result

print(main(inpt))