from pyquery import PyQuery as pq

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
doc = pq(text)
li = doc(".item-0.active")
print(li)
li.remove_class("item-0")
print(li)
li.add_class("item-1")
print(li)
print(li.text())
print("-----------")
li.attr("name", "link")
print(li)
li.text("changed item")
print(li)
li.html("<span>changed item</span>")
print(li)
print(li.text())
print(li.html())


















