#https://timber.io/blog/an-intro-to-web-scraping-with-lxml-and-python/
def HTMLParser1():
    import requests
    import lxml.html

    html = requests.get('https://coinmarketcap.com/new/')
    doc = lxml.html.fromstring(html.content)

    #retunrs a list of all divs in HTML page which have an id of tab_newrelease_content
    #new_releases = doc.xpath('.//a[@class="cmc-link"]/text()')
    newest_release= doc.xpath('//*[@id="__next"]/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]/a[@class="cmc-link"]/@href')
    print(newest_release)

    #// these double forward slashes tell lxml that we want to search for all tags in the HTML document which match our requirements/filters. Another option was to use / (a single forward slash). The single forward slash returns only the immediate child tags/nodes which match our requirements/filters
    return newest_release


#XPATH1: //*[@id="__next"]/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]/a
#Xpath2: //*[@id="__next"]/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[3]/a
#XPath Element1 whole row: //*[@id="__next"]/div/div/div[2]/div/div[2]/table/tbody/tr[1]
#FULL XPATH1: /html/body/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]/a

