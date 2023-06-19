# parser = 구문 분석 / 태그 제거
from urllib.request import urlopen
from html.parser import HTMLParser

class ImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)

def parse_image(data):
    parser = ImageParser()
    parser.feed(data)
    dataSet = set(x for x in parser.result)
    return dataSet

def main():
    url = 'https://google.co.kr'
    with urlopen(url) as f:
        charset = f.headers.get_params('charset')[1][1]
        data = f.read().decode(charset)

    data_set = parse_image(data)
    print('\n>>>>> Fetch Image from', url)
    print('\n'.join(sorted(data_set)))

if __name__ == '__main__':
    main()



