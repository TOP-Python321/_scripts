from abc import ABC
from itertools import chain
from pathlib import Path
from re import compile, Pattern
from sys import path


class TextParser(ABC):
    bold_pat: Pattern
    italic_pat: Pattern
    underline_pat: Pattern

    def find_all_bold(self, text: str) -> list[str]:
        return self.bold_pat.findall(text)

    def find_all_italic(self, text: str) -> list[str]:
        return self.italic_pat.findall(text)

    def find_all_underline(self, text: str) -> list[str]:
        return self.underline_pat.findall(text)


class HTML(TextParser):
    bold_pat = compile(r'<strong>(.*?)</strong>')
    italic_pat = compile(r'<i>(.*?)</i>')
    underline_pat = compile(r'<u>(.*?)</u>')


class Markdown(TextParser):
    bold_pat = compile(r'(\*\*(.*?)\*\*)|(__(.*?)__)')
    italic_pat = compile(r'(\*(.*?)\*)|(_(.*?)_)')
    underline_pat = None



def parse_text(parser: TextParser, text: str):
    emphasis = chain(
        parser.find_all_bold(text),
        parser.find_all_italic(text),
        parser.find_all_underline(text),
    )
    for substr in emphasis:
        print(substr)


example_path = Path(path[0]) / '_TextParser_example.txt'
parse_text(HTML(), example_path.read_text())
