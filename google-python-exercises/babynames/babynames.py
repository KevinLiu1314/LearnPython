#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  baby_names={}
  try:
    f=open(filename,'r')
  except:
    print("Can't open file:", filename)
    return {}
    
  text=f.read()
  f.close()
  
  year=re.findall(r'Popularity in ([\d]{4})', text)
  year_ranks=re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)

  for rank in year_ranks:
    baby_names[(int(year[0]), int(rank[0]))]=(rank[1], rank[2])
  
  return baby_names

def query(baby_names):
  """ Queries the baby_names database interactively """
  while True:
    response = raw_input("Enter YEAR, RANK('q' to quit): ")
    if response == 'q': break
    
    try:
      (year, rank)=response.split(',')
    except:
      print('Invalid response')
      continue
        
    (year, rank)=(int(year), int(rank))
    if (year, rank) in baby_names:
      print(baby_names[(year, rank)])
    else:
      print('No Data for year:{year}, rank:{rank}'.format(year=year, rank=rank))

def print_summary(baby_names):
  """
  Prints a list of baby names sorted alphabetically follow by it's rank in the year
  Generate a summary file for each year in the baby_name database
  """
  years = []
  for key in baby_names.keys():
    if not str(key[0]) in years: years.append(str(key[0]))

  for year in years:
    list = [year]
    for key in baby_names.keys():
      if key[0] == int(year):
        list.append(baby_names[key][0] + '(Boy): ' + str(key[1]))
        list.append(baby_names[key][1] + '(Girl): ' + str(key[1]))

    list = sorted(list)
    text = '\n'.join(list) + '\n'
    f = open("baby" + year + '.summary', 'w')
    f.write(text)
    f.close

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  baby_names={}
  for filename in args:
    baby_names.update(extract_names(filename))

  query(baby_names)

  if summary:
    print_summary(baby_names)
  
if __name__ == '__main__':
  main()
