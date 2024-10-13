class Finglish:
    def __init__(self):
        self.char = [
            ['ض', 'z'], ['ص', 's'], ['ث', 's'], ['ق', 'gh'], ['ف', 'f'], ['غ', 'gh'], ['ا', 'a'], ['ه', 'h'], ['خ', 'kh'], ['ح', 'h'], ['ج', 'j'], ['چ', 'ch'],
            ['پ', 'p'], ['ش', 'sh'], ['س', 's'], ['ی', 'i'], ['ب', 'b'], ['ل', 'l'], ['ع', 'a'], ['ت', 't'], ['ن', 'n'], ['م', 'm'], ['ک', 'k'], ['گ', 'g'],
            ['ظ', 'z'], ['ط', 't'], ['ز', 'z'], ['ر', 'r'], ['ذ', 'z'], ['د', 'd'], ['و', 'v'], ['ژ', 'zh'], ['ی', 'y']
        ]
    
    def persian_to_english(self, text):
        for i in text:
            for c in self.char:
                if c[0] == i:
                    text = text.replace(i, c[1])
        return text
    
    def english_to_persian(self, text):
        for i in text:
            for c in self.char:
                if c[1] == i:
                    text = text.replace(i, c[0])
        return text