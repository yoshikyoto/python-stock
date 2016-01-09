import urllib2

class HttpRequest:
    @staticmethod
    def get(url):
        buf = urllib2.urlopen(url)
        return buf.read()

if __name__ == '__main__':
    html = HttpRequest.get('http://stocks.finance.yahoo.co.jp/stocks/detail/?code=7550.T')
    print html
