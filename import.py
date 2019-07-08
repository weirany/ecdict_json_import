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
output_filename = 'words_frq_only_one_trans.json'
include_bnc = False
include_frq = True
include_all = False
one_translation_only = True

with open(input_filename) as csvfile:
    defs = []
    reader = csv.reader(csvfile)
    skipped_header_row = False
    print('starting loop')
    for row in reader:
      if not skipped_header_row:
        skipped_header_row = True
        continue
      # only take these fields: 0 - word; 3 - translation; 8 - bnc; 9 - frq
      word = row[0]
      translation = row[3]
      bnc = int(row[8])
      frq = int(row[9])
      is_skip = True
      if include_all or (include_bnc and bnc != 0) or (include_frq and frq != 0):
        is_skip = False
      if not is_skip:
        if one_translation_only:
          translation = translation.split('\\n')[0].split('\\r')[0]
        definition = Definition(word, translation, bnc, frq)
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
