from googletrans import Translator as GoogleTranslator

class TextTranslator:
    def __init__(self, target_lang="ko"):
        self.translator = GoogleTranslator()
        self.target_lang = target_lang

    def translate(self, text):
        try:
            return self.translator.translate(text, dest=self.target_lang).text
        except Exception:
            return "[error]"