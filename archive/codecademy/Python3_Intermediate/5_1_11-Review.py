# Learn Intermediate Python 3
# 5. Unit Testing
# 1. Exceptions
# 11. Review

print('''\n
Review
------- ''')

# Congragulations, you have now mastered many techniques for interacting with
# exceptions in Python! We learned:
#
#   - How exceptions differ from syntax errors
#
#   - How to read tracebacks
#
#   - How try/except/else/finally provides us with a powerful control
#     flow for handling exceptions
#
#   - How to create and raise custom exceptions to provide more helpful
#     errors to users of our code
#
# These tools will get you very far as a Python developer!

# Taks
# 1. The code in families.py prints some instruments and the instrument 
#    families they belong to. It has some bugs in it. Can you find and fix
#    the bugs? Consider adding some exception handlers so that you
#    can print custom error messages the next time someone runs into
#    these bugs!

instrument_familes = {
  'Strings': ['Guitar', 'Banjo', 'Sitar'],
  'Percussion': ['Conga', 'Cymbal', 'Cajon'],
  'Woodwinds': ['Flute', 'Oboe', 'Clarinet']
}

def print_instrument_families():
  for family in ['Strings', 'Percussion', 'Woodwinds']:
    print('Some instruments in the ' + family + 'family are: ' + str(instrument_familes[family]))

try:
  print_instrument_families()
except KeyError:
  print('Typos, did you check lower/upper/title case?')
except TypeError:
  print('Check if you missed a str() function')