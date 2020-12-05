import re

import utils

input = utils.getInput(4).split("\n\n")

passports = [s.replace("\n", " ").split(" ") for s in input]

hairPattern = re.compile("^#[0-9a-f]{6}$")
pidPattern = re.compile("^[0-9]{9}$")


def cmVal(v):
    return v[-2:] == "cm" and int(v[:-2]) >= 150 and int(v[:-2]) <= 193


def inVal(v):
    return v[-2:] == "in" and int(v[:-2]) >= 59 and int(v[:-2]) <= 76


validation = {
    "byr": lambda v: int(v) >= 1920 and int(v) <= 2002,
    "iyr": lambda v: int(v) >= 2010 and int(v) <= 2020,
    "eyr": lambda v: int(v) >= 2020 and int(v) <= 2030,
    "hgt": lambda v: cmVal(v) or inVal(v),
    "hcl": lambda v: bool(hairPattern.match(v)),
    "ecl": lambda v: v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda v: bool(pidPattern.match(v)),
    "cid": lambda v: True,
}

validPassports = 0
validPassportsData = 0
for passport in passports:
    hasField = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False,
        "cid": True,
    }
    validData = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False,
        "cid": True,
    }

    for field in passport:
        pair = field.split(":")

        hasField[pair[0]] = True
        validData[pair[0]] = validation[pair[0]](pair[1])

    if all(hasField.values()):
        validPassports += 1

    if all(validData.values()):
        validPassportsData += 1

print(f"part 1: {validPassports}")
print(f"part 2: {validPassportsData}")
