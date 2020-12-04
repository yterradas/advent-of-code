import sys, functools
import re

def isvalidp1(passport, allowmissing={}):
  passportlen = len(passport)
  if passportlen == 8: return True
  if passportlen == 7 and not allowmissing.issubset(passport.keys()): return True
  return False


def isvalidp2(passport):
  passportlen = len(passport)
  if passportlen < 7: return False
  if passportlen == 7 and {'cid'}.issubset(passport.keys()): return False

  if len(passport['byr']) != 4: return False
  byrval = int(passport['byr'])
  if byrval < 1920 or byrval > 2002: return False

  if len(passport['iyr']) != 4: return False
  iyrval = int(passport['iyr'])
  if iyrval < 2010 or iyrval > 2020: return False

  if len(passport['eyr']) != 4: return False  
  eyrval = int(passport['eyr'])
  if eyrval < 2020 or eyrval > 2030: return False

  hgtval = passport['hgt']
  if hgtval[-2::] not in ['in','cm']: return False
  elif 'in' == hgtval[-2::]:
    v = int(hgtval.strip('in'))
    if v < 59 or v > 76: return False
  elif 'cm' == hgtval[-2::]:
    v = int(hgtval.strip('cm'))
    if v < 150 or v > 193: return False
    
  hclval = passport['hcl']
  match = re.search("^#[0-9a-f]{6}$", hclval)
  if match is None or match[0] != hclval: return False

  if passport['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']: return False

  pidval = passport['pid']
  match = re.search("^[0-9]{9}$", pidval)
  if match is None or match[0] != pidval: return False
  
  return True


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
      if isvalidp1(passportfields, allowmissing={'cid'}):
        validpassports += 1
      passport = ''
      continue
    passport += ' ' + line
  if passport != '':
    passportfields = parsefields(passport.lstrip(' '))
    if isvalidp1(passportfields, allowmissing={'cid'}):
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
