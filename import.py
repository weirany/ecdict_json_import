import csv
import json
import jsonpickle

class Definition:
  def __init__(self, word, translation, bnc, frq):
    self.w = word
    self.t = translation
    self.b = bnc
    self.f = frq

input_filename = 'ecdict.csv'
output_filename = 'words_frq_only.json'
include_bnc = False
include_frq = True
include_all = False

with open(input_filename) as csvfile:
    defs = []
    reader = csv.reader(csvfile)
    skipped_header_row = False
    print('starting loop')
    for row in reader:
      if not skipped_header_row:
        skipped_header_row = True
        continue
      is_skip = True
      if include_all or (include_bnc and row[8] != '0') or (include_frq and row[9] != '0'):
        is_skip = False
      if not is_skip:
        # only take these fields: 0 - word; 3 - definition; 8 - bnc; 9 - frq
        definition = Definition(row[0], row[3], int(row[8]), int(row[9]))
        defs.append(definition)
    print('end loop')
    sorted_defs = sorted(defs, key=lambda x: x.f)
    print('end sorting')
    jsonpickle.set_encoder_options('json', ensure_ascii=False)
    json_words = jsonpickle.encode(sorted_defs, unpicklable=False)
    print('end serialization')
    with open(output_filename, 'w') as words_fle:
      words_fle.write(json_words)
    print('end')
