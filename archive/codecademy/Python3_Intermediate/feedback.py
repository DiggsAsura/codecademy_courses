class FormError(Exception):
  pass

def issue_survey():
  print('Opening customer survey')
  raise FormError('An error occured when opening customer survey form!')

def log_customer_complaint():
  print('Opening customer complaint form')
  print('Logged customer complaint')
  return 'Success'