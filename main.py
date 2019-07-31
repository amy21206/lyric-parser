from musicxml_parser import MusicXMLDocument 
import json

# parses lyrics.

def main():
  score_parser = MusicXMLDocument('A_Broken_Hallelujah.xml')

  result = {}
  parts = {}
  for part in score_parser.parts:
    info_list = []
    for measure in part.measures:
      for note in measure.notes:
        if note.has_lyric:
          info_list.extend(note.get_pitch_and_lyric_list())
    info_list.sort(key=lambda x: x['number'])
    lyric_list = {}
    cnt = 0
    for info in info_list:
      lyric_list[cnt] = info['info']
      cnt += 1
    parts[part.score_part.part_name] = lyric_list
  result['Parts'] = parts

  # dumps json in file
  with open('output.txt', 'w') as f:
    # dumps in a machine-readable format
    json.dump(result, f)

if __name__ == '__main__':
  main()