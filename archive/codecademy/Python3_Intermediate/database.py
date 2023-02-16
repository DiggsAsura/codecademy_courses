# Follow file for 5_1_8-The_finally_Clause.py

instruments = {
  'Kora': {
    'Family': 'Strings',
    'Origin': 'West Africa',
  },
  'Didgeridoo': {
    'Family': 'Wind',
    'Origin': 'Northern Australia',
  },
  'Guitar': {
    'Family': 'Strings',
    'Origin': 'Spain',
  }
}

def connect_to_database():
  print('Establishing connection to instrument database server...')

def disconnect_from_database():
  print('Destroying connection to instrument database server...')

def get_instrument_info(instrument):
  return instruments[instrument]

def display_instrument_info(instrument):
  info = get_instrument_info(instrument)
  print('Instrument: ' + info['Family'])
  print('Origin: ' + info['Origin'])
  