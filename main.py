### Assignment: Regex and Files
##Name: Amir
##Date: Feb 22

#don't forget to import regex


##(/5) Task 1: MODIFY the code below.
#A# Change the regex from .* to what is required to capture an email address
#B# Add a condition so that no blanks are printed.
#C# Count the number of email addresses found and print a final output line.
import re

def reEmail(fname):
  count = 0
  fhand = open(fname,'r')
  for line in fhand:
    extr = re.findall('\S+@\S+',line)
    if len(extr): 
      count += 1
      print(extr)
  print(count)
        

  print()
   

'''### Task 1 Results for 
>reEmail('rural-staff.txt')
['demcisaac@edu.pe.ca']
...
['pewynne@edu.pe.ca']
There were 89 email addresses in rural-staff.txt 
### '''

##(/5) Task 2: MODIFY code that will open the athletics file and extract all award winners
#notice that in the rural-athletics.txt file, the pattern is "... - AWARD WINNER(S)"
#You should use a ( and ) regex like " (extract this) " to extract a portion of the match

def reAward(fname):
  fhand = open(fname, 'r')
  for line in fhand:
    extr = re.findall('-.+', line)
    if len(extr):
      print(extr)

'''### Task 2 Results for
>reAward('rural-athletics.txt')
['Devon Lawlor']
...
['Jose Crisostomo, Kalon MacDonald-Wood'] 
###'''

##(/5) Task 3: CREATE code that will open a file and extract all the phone numbers 

def rePhone(fname):
  fhand = open(fname, 'r')
  for line in fhand:
    extr = re.findall('[0-9]{3,}-\S+', line)
    if len(extr):
      print(extr)
  #open file
  #loop through the file
  #extract the specific phone numbers regex
  #if the length of the extraction is not empty
  #print the phone number

'''### Task 3 results
>rePhone('rural-staff.txt')
['902-368-6905']
###'''
