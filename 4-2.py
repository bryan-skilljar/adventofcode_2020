import re

with open('/Users/bryanlarson/Documents/scripts/adventofcode_2020/4.txt', 'r') as f:
    text = f.read()

passports = text.split('\n\n')

required_fields = {
    'byr': '^(19[2-9][0-9]|200[0-2])$',
    'iyr': '^(201[0-9]|2020)$',
    'eyr': '^(202[0-9]|2030)$',
    'hgt': '^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$',
    'hcl': '^#[0-9a-f]{6}$',
    'ecl': '^(amb|blu|brn|gry|grn|hzl|oth)$',
    'pid': '^\d{9}$',
}

total_valid = 0

for p in passports:
    data = {f.split(':')[0]: f.split(':')[1] for f in p.split()}

    if all(key in data and re.match(value, data[key]) for key, value in required_fields.items()):
        total_valid += 1

print(total_valid)
