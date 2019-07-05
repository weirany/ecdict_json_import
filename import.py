import csv
import json
import jsonpickle

class Definition:
  def __init__(self, word, translation, bnc, frq):
    self.word = word
    self.translation = translation
    self.bnc = bnc
    self.frq = frq

input_filename = 'ecdict.csv'
output_filename = 'words_frq_only.json'
include_bnc = False
include_frq = True
include_all = False

with open(input_filename) as csvfile:
    defs = []
    reader = csv.reader(csvfile)
    print('starting loop')
    for row in reader:
      is_skip = True
      if include_all or (include_bnc and row[8] != '0') or (include_frq and row[9] != '0'):
        is_skip = False
      if not is_skip:
        # only take these fields: 0 - word; 3 - definition; 8 - bnc; 9 - frq
        definition = Definition(row[0], row[3], row[8], row[9])
        defs.append(definition)
    print("end loop")
    jsonpickle.set_encoder_options('json', ensure_ascii=False)
    json_words = jsonpickle.encode(defs, unpicklable=False)
    print('end serialization')
    with open(output_filename, 'a') as words_fle:
      words_fle.write(json_words)
    print('end')
