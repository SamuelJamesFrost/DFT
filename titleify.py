import re

file = 'references.bib'

def title_case(string):
    string = (string.title()
        .replace(' And ', ' and ')
        .replace(' Or ', ' or ')
        .replace(' In ', ' in ')
        .replace(' Of ', ' of ')
        .replace(' With ', ' with ')
        .replace('The ', 'the ')
        .replace('A ', 'a ')
        .replace(' For ', ' for ')
        .replace('Van Der ', 'van der '))
    return string[0].upper() + string[1:]

with open(file, 'r') as f:
    for line in f.readlines():
        match = re.search(r'(?i)\s*(journal|title)\s*=\s*\{*', line)
        if match:
            title_start = match.span()[1]
            line = line[:title_start] + title_case(line[title_start:])

        print(line, end='')
