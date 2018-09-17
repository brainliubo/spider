from lxml import etree

# text = '''
# <div>
# <Ul>
# <li class="item-O"><a href="linkl.html">first item</a></li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-inactive"><a href="link3.html">third item</a></h>
# <li class="item-1"><a href="link4.html">fourth item</a></li>
# <li class ＝"item"><a href＝"links.html">item</a>
# </ul>
# </div>
# '''
# html = etree.HTML(text)
#
# result= etree.tostring(html)
# result_1 = (result.decode("utf-8"))
#
# with open("lxml_test.html","w") as f:
#     f.writelines(result_1)

html = etree.parse("lxml_test.html",etree.HTMLParser())
print(type(html))
print(html.xpath('//ul//li[contains(@class,"kkk")]//text()'))