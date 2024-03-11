class MorseConverter(object):
    def __init__(self):
        self.codes = {
            '1': '.----.',
            '2': '..---.',
            '3': '...--.',
            '4': '....-.',
            '5': '......',
            '6': '-.....',
            '7': '--....',
            '8': '---...',
            '9': '----..',
            '0': '-----.',
        }

    def to(self, str):
        return ''.join([self.codes[c] for c in str])
