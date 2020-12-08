with open('/Users/bryanlarson/Documents/scripts/adventofcode_2020/4.txt', 'r') as f:
    text = f.read()

passports = text.split('\n\n')

required_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]

total_valid = 0

for p in passports:
    data = {f.split(':')[0]: f.split(':')[1] for f in p.split()}

    if all(f in data for f in required_fields):
        total_valid += 1

print(total_valid)
