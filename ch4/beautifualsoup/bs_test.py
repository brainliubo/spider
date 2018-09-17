

from bs4 import BeautifulSoup as bs

txt = '''
<html>
<head><title>bs_test_html</title></head>
<body><div>
<ul>
<li class="item-O"><a href="linkl.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive kkk"><a href="link3.html">third item</a></li>
    <li class="item-1"><a href="link4.html">fourth item</a></li>
<li><a href="">item</a>
</li></ul>
</div>
</body></html>


'''


soup = bs(txt,"lxml")
print(type(soup))

print(soup.prettify())
print((soup.title.string))
print(soup.head)
print(soup.div.ul.li)