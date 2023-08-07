from itertools import chain
from pathlib import Path
from re import compile
from sys import path


class HTML:
    patterns = {
        'emphasis': (
            compile(r'<strong>(.*?)</strong>'),
            compile(r'<em>(.*?)</em>'),
            compile(r'<u>(.*?)</u>')
        ),
        # ...
    }

    def extract_emphasis(self, text: str) -> list[str]:
        result = []
        for pat in self.patterns['emphasis']:
            result += pat.findall(text)
        return result


class Markdown:
    bold_pat = compile(r'\*\*(.*?)\*\*|__(.*?)__')
    italic_pat = compile(r'\*(.*?)\*|_(.*?)_')
    # ...

    def extract_emphasis(self, text: str) -> list[str]:
        return list(
            substr
            for substr in chain(
                *self.bold_pat.findall(text),
                *self.italic_pat.findall(text)
            )
            if substr
        )


def parse_text(parser: HTML | Markdown, text: str):
    for substr in parser.extract_emphasis(text):
        print(substr)



example_path = Path(path[0]) / '_TextParser_example.txt'
parse_text(Markdown(), example_path.read_text())
