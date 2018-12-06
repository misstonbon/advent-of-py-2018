import string
import re

###################### DISREGARD ###########################

upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
zip_upper_lower = list(zip(upper, lower))
zip_lower_upper = list(zip(lower, upper))
combos = set()
for a, b in zip_upper_lower:
    combos.add(''.join([a,b]))

for a, b in zip_lower_upper:
    combos.add(''.join([a,b])) 

REGEX = ""

rgx_list = []
for combo in combos:
    rgx_list.append(combo)

for combo in combos:
    REGEX += "|%s" %combo


with open('./dayfive.txt', 'r') as content_file:
    file_string = str(content_file.read())

pattern = re.compile("%s" % REGEX)
result = re.findall(pattern, file_string)
result[:] = [item for item in result if item != '']

def clean_text(rgx = rgx_list, text = file_string, rgx_str = REGEX):
    pattern = re.compile(rgx_str)
    result = re.findall(pattern, file_string)
    result[:] = [item for item in result if item != '']
    new_text = text
    while True:
        for rgx_match in rgx_list:
            new_text = re.sub(rgx_match, '', new_text)
            print(len(new_text))


# clean_text()

#################################################################

def react(input_string):
    result = []
    for char in input_string:
        if len(result) > 0 and abs(ord(char) - ord(result[-1])) == 32:
            result.pop()
        else:
            result.append(char)
    return len(result)

def collapse(input_string):
    min_after_collapsed = None
    for char in string.ascii_lowercase:
        stack = []
        s = input_string.replace(char, "")
        s = s.replace(char.upper(), "")
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            elif stack[-1].lower() == char.lower() and stack[-1] != char:
                stack.pop()
            else:
                stack.append(char)
        if min_after_collapsed is None or min_after_collapsed > len(stack):
            min_after_collapsed = len(stack)
    return min_after_collapsed

print(collapse(file_string))