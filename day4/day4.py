input_file = open('day4.txt', 'r')
lines = input_file.readlines()

total_passports = 0
valid_passports = 0
passport = ""
for line in lines:
    passport += line
    if line == '\n':
        total_passports += 1
        fields = {}
        valid = True
        passport = passport.replace('\n', ' ')
        tokens = passport.split(' ')
        for token in tokens:
            if token != '':
                kv = token.split(':')
                fields[kv[0]] = kv[1]
        if "byr" in fields:
            value = fields["byr"]
            if len(value) != 4:
                valid = False
            if int(value) < 1920 or int(value) > 2002:
                valid = False
        else:
            valid = False
        if "iyr" in fields:
            value = fields["iyr"]
            if len(value) != 4:
                valid = False
            if int(value) < 2010 or int(value) > 2020:
                valid = False
        else:
            valid = False
        if "eyr" in fields:
            value = fields["eyr"]
            if len(value) != 4:
                valid = False
            if int(value) < 2020 or int(value) > 2030:
                valid = False
        else:
            valid = False
        if "hgt" in fields:
            value = fields["hgt"]
            if 'cm' in value:
                num = value.split('cm')[0]
                try:
                    if int(num) > 193 or int(num) < 150:
                        valid = False
                except:
                    valid = False
            elif 'in' in value:
                num = value.split('in')[0]
                try:
                    if int(num) > 76 or int(num) < 59:
                        valid = False
                except:
                    valid = False
            else:
                valid = False
        else:
            valid = False
        if "hcl" in fields:
            value = fields["hcl"]
            if '#' in value:
                val = value.split('#')[1]
                if len(val) != 6 or not val.isalnum():
                    valid = False
            else:
                valid = False
        else:
            valid = False
        if "ecl" in fields:
            value = fields["ecl"]
            if not value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                valid = False
        else:
            valid = False
        if "pid" in fields:
            value = fields["pid"]
            if len(value) != 9 or not value.isnumeric():
                valid = False
        else:
            valid = False

        if valid:
            valid_passports += 1
        passport = ""

print(f"total passports: {total_passports}")
print(f"valid passports: {valid_passports}")
