text = '''
<div>
<ul>
<li class = "item-0"><a href = "link1.html">first item</a><li>
<li class = "item-1"><a href = "link2.html">second item</a><li>
<li class = "item-0 active"><a href = "link3.html">third item</a><li>
<li class = "item-1"><a href = "link4.html">fourth item</a><li>
<li class = "item-0"><a href = "link5.html">fifth item</a>3
</ul>
</div>
'''

from pyquery import PyQuery as pq
doc = pq(text)
li = doc("li:first-child")
print(li)
print("----------------")
li = doc("li:last-child")
print(li)
print("----------------")
li = doc("li:nth-child(2)")
print(li)
print("----------------")
li = doc("li:gt(2)")
print(li)
print("----------------")
li = doc("li:nth-child(2n)")
print(li)
print("----------------")
li = doc("li:contains(second)")
print(li)
print("----------------")


















