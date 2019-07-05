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
include_bnc_only = False
include_frq_only = True

with open(input_filename) as csvfile:
    defs = []
    reader = csv.reader(csvfile)
    print('starting loop')
    for row in reader:
      if (include_bnc_only and row[8] == '0'):
        continue
      if (include_frq_only and row[9] == '0'): 
        continue
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
