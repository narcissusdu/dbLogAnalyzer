from pathlib2 import Path
import re


class DBLogAnalyzer(object):
    log_path = ''
    language = ''
    pattern_ancient_string = {
        'cn': r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}).+(\b[\u4e00-\u9fa5]+(?= 掉落)).+(?=远古=True).*?(?<=太古=)(.).*?((?<=原始类型=).+).*?\n',
        'en': r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}).+(\b[\u4e00-\u9fa5]+(?= dropped)).+(?=Ancient=True).*?(?<=Primal=)(.).*?((?<=RawType=).+).*?\n'
    }

    def __init__(self, log_path, language):
        self.log_path = log_path
        self.language = language

    def start(self):
        content = Path(self.log_path).read_text()
        pattern_ancient = re.compile(self.pattern_ancient_string[self.language])
        matches = pattern_ancient.findall(content)

        ancient = []
        primal = []
        for match in matches:
            if match[2] == 'T':
                primal.append(match)
            else:
                ancient.append(match)

        print("\n\nPrimal:\t(%d in total)\n\n" % (len(primal)))

        for item in primal:
            print("%s %s %s\n" % (item[1].rjust(15), item[3].rjust(15), item[0].rjust(15)))

        print("\n\nAncient:\t(%d in total)\n\n" % (len(ancient)))

        for item in ancient:
            print("%s %s %s\n" % (item[1].rjust(15), item[3].rjust(15), item[0].rjust(15)))
