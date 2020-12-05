import sys, functools
import re

def hasrequiredfields(passport):
  passportlen = len(passport)
  if passportlen < 7: return False
  if passportlen == 7 and {'cid'}.issubset(passport.keys()): return False
  return True


def isbyrvalid(field):
  if len(field) != 4: return False
  byrval = int(field)
  if byrval < 1920 or byrval > 2002: return False
  return True


def isiyrvalid(field):
  if len(field) != 4: return False
  iyrval = int(field)
  if iyrval < 2010 or iyrval > 2020: return False
  return True


def iseyrvalid(field):
  if len(field) != 4: return False  
  eyrval = int(field)
  if eyrval < 2020 or eyrval > 2030: return False
  return True


def ishgtvalid(field):
  if field[-2::] not in ['in','cm']: return False
  elif 'in' == field[-2::]:
    v = int(field.strip('in'))
    if v < 59 or v > 76: return False
  elif 'cm' == field[-2::]:
    v = int(field.strip('cm'))
    if v < 150 or v > 193: return False
  return True


def ishclvalid(field):
  match = re.search("^#[0-9a-f]{6}$", field)
  if match is None or match[0] != field: return False
  return True


def iseclvalid(field):
  return field in ['amb','blu','brn','gry','grn','hzl','oth']


def ispidvalid(field):
  match = re.search("^[0-9]{9}$", field)
  if match is None or match[0] != field: return False
  return True

  
def isvalidp2(passport):
  if not hasrequiredfields(passport): return False

  return isbyrvalid(passport['byr']) \
     and isiyrvalid(passport['iyr']) \
     and iseyrvalid(passport['eyr']) \
     and ishgtvalid(passport['hgt']) \
     and ishclvalid(passport['hcl']) \
     and iseclvalid(passport['ecl']) \
     and ispidvalid(passport['pid'])


def parsefields(line):
  d = {}
  for fields in line.split(' '):
    f = fields.split(':')
    d[f[0]] = f[1]
  return d
  
 
def part1(filename):
  with open(filename) as f:
    lines = [l.rstrip('\n') for l in f.readlines()]

  validpassports = 0
  passport = ''
  for line in lines:
    if line == '':
      passportfields = parsefields(passport.lstrip(' '))
      if hasrequiredfields(passportfields):
        validpassports += 1
      passport = ''
      continue
    passport += ' ' + line
  if passport != '':
    passportfields = parsefields(passport.lstrip(' '))
    if hasrequiredfields(passportfields):
      validpassports += 1
  
  print(f"part1 >>> Santa has {validpassports} valid passports")


def part2(filname):
  with open(filename) as f:
    lines = [l.rstrip('\n') for l in f.readlines()]

  validpassports = 0
  passport = ''
  for line in lines:
    if line == '':
      passportfields = parsefields(passport.lstrip(' '))
      if isvalidp2(passportfields):
        validpassports += 1
      passport = ''
      continue
    passport += ' ' + line
  if passport != '':
    passportfields = parsefields(passport.lstrip(' '))
    if isvalidp2(passportfields):
      validpassports += 1
    
  print(f"part2 >>> Santa has {validpassports} valid passports")
  

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
