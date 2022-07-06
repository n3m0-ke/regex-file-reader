# import required module
from pathlib import Path
import re
 
# assign directory
directory = 'pfb_ind_assign2'
 
# iterate over files in
# that directory
files = Path(directory).glob('*.txt')

for file in files:
  print (file.name)
  infile = open(file, 'r')
  lines = infile.readlines()

  details_list = []

  address = ""
  flat_type = ""
  start_date = ""
  end_date = ""
  rent = ""

  for line in lines:
    if re.match("2. ADDRESS OF THE FLAT", line):
      address = re.search('2. ADDRESS OF THE FLAT: (.*)', line).group(1)
      details_list.append(address)

    if re.match("3. TYPE OF FLAT", line):
      flat_type = re.search('3. TYPE OF FLAT: (.*)', line).group(1).strip()
      details_list.append(flat_type)
    
    if re.match("7. PERIOD OF THE TENANCY: ", line):
      start_date = re.search('days commencing  on  (.+*) and expiring on', line).group(1)
      end_date = re.search('and expiring on  (.+*)', line).group(1)

      print(start_date)

      details_list.append(start_date)
      details_list.append(end_date)
    
    if re.match("8. RENT", line):
      rent = re.search("rent amount is (.*) per month payable", line).group(1)
      details_list.append(rent)

  print(details_list)