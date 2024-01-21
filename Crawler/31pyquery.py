
from pyquery import PyQuery as pq

text = '''
<div>
<ul>
<li class = "item-0"><a href = "link1.html">first item</a><li>
<li class = "item-1"><a href = "link2.html">second item</a><li>
<li class = "item-inactive"><a href = "link3.html">third item</a><li>
<li class = "item-1"><a href = "link4.html">fourth item</a><li>
<li class = "item-0"><a href = "link5.html">fifth item</a>3
</ul>
</div>
'''

doc = pq(text)
print(doc("li"))

doc1 = pq(url="https://cuiqingcai.com")
print(doc1("title"))
