
def calc(entry_list):

  if "(" in entry_list:

    if entry_list.count("(") == entry_list.count(")"):
      
     entry_list = paranth_simp(entry_list)

    else: 
      print("Invalid syntax")

  # run calc_add_innards on all sects outside paratheses
  if "+" in entry_list or "-" in entry_list:
    entry_list = calc_add_innards(entry_list)
    return entry_list
    
  # run calc_mult_innards on all sects without add_sub
  if "*" in entry_list or "/" in entry_list:
      entry_list = calc_mult_innards(entry_list)
      return entry_list

  # run calc_exp_innards on all sects without mult_div
  if "^" in entry_list:
    entry_list = calc_exp_innards(entry_list)
    return entry_list

  return entry_list

# simplify parantheses
def paranth_simp(entry_list):

  # find location of pairs
  start = entry_list.index("(")
  end = entry_list.rindex(")")

  innards = entry_list[start+1:end]

  # calculate innards of those pairs (recursive)
  next_entry = []
  next_entry.append(entry_list[0:start])
  next_entry.append("")
  next_entry.append(entry_list[end+1:len(entry_list)])
  next_entry[1] = calc(innards)
  next_entry = [str(elem) for elem in next_entry]
  next_entry = "".join(next_entry)

  return next_entry

# calculate additive innards
def calc_add_innards(entry_list):  
  # find locations of all addition/subtraction signs
  signs_loc = get_list_of_signs(entry_list, ["+", "-"])

  # create new list of lists split at the signs_loc
  entry_split_add_sub = []
  prev = 0
  for sign in signs_loc:
    key = entry_list.index(sign, prev)
    entry_split_add_sub.append(entry_list[prev:key])
    prev = key+1
  
  # add in final split not covered by above for loop
  entry_split_add_sub.append(entry_list[prev:len(entry_list)])
  
  # calculate multiplicative innards
  entry_split_add_sub = [str(elem) for elem in entry_split_add_sub]
  for index, entry in enumerate(entry_split_add_sub):
    if "*" in entry or "/" in entry:
      entry_split_add_sub[index] = calc_mult_innards(entry)
  
  entry_split_add_sub = [str(elem) for elem in entry_split_add_sub]
  for index, entry in enumerate(entry_split_add_sub):
    if "^" in entry:
      entry_split_add_sub[index] = calc_exp_innards(entry)

  # iterate over entry_split_add_sub and cross reference with signs_loc to calculate
  while len(entry_split_add_sub) > 1:
    for val in signs_loc:
      if val == "+":
        entry_split_add_sub[0] = float(entry_split_add_sub[0]) + float(entry_split_add_sub[1])
      elif val == "-":
        entry_split_add_sub[0] = float(entry_split_add_sub[0]) - float(entry_split_add_sub[1])
      else: 
        print("ERROR")
      del entry_split_add_sub[1]
  
  return entry_split_add_sub[0]

# calculate multiplicative innards
def calc_mult_innards(entry_list):

  # find multiplications / divisions
  signs_loc = get_list_of_signs(entry_list, ["*", "/"])

  # split at newly found locations
  entry_split_mult_div = []
  prev = 0
  for sign in signs_loc:
    key = entry_list.index(sign, prev)
    entry_split_mult_div.append(entry_list[prev:key])
    prev = key+1
    
  # add in final split not covered by above for loop
  entry_split_mult_div.append(entry_list[prev:len(entry_list)])
  
  # calculate exponential innards
  entry_split_mult_div = [str(elem) for elem in entry_split_mult_div]
  for index, entry in enumerate(entry_split_mult_div):
    if "^" in entry:
      entry_split_mult_div[index] = calc_exp_innards(entry)

    
  # iterate over entry_split_ and cross reference with signs_loc to calculate
  while len(entry_split_mult_div) > 1:
    for val in signs_loc:
      if val == "*":
        entry_split_mult_div[0] = float(entry_split_mult_div[0]) * float(entry_split_mult_div[1])
      elif val == "/":
        entry_split_mult_div[0] = float(entry_split_mult_div[0]) / float(entry_split_mult_div[1])
      else: 
        print("ERROR")
      del entry_split_mult_div[1]
  
  return entry_split_mult_div[0]

# calculate exponential innards
def calc_exp_innards(entry_list):

  # find exponentials
  signs_loc = get_list_of_signs(entry_list, ["^"])

  # split at newly found locations
  entry_split_exp = []
  prev = 0
  for sign in signs_loc:
    key = entry_list.index(sign, prev)
    entry_split_exp.append(entry_list[prev:key])
    prev = key+1
    
  # add in final split not covered by above for loop
  entry_split_exp.append(entry_list[prev:len(entry_list)])
    
  # iterate over entry_split_ and cross reference with signs_loc to calculate
  while len(entry_split_exp) > 1:
    for val in signs_loc:
      if val == "^":
        entry_split_exp[0] = float(entry_split_exp[0]) ** float(entry_split_exp[1])
      else: 
        print("ERROR")
      del entry_split_exp[1]
  
  return entry_split_exp[0]

def get_list_of_signs(entry_list, signs):

  ordered_signs = []

  for entry in entry_list:
    if entry in signs:
      ordered_signs.append(entry)

  # return dictionary {index of sign: sign}
  return ordered_signs