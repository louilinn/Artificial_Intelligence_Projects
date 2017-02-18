from anytree import Node, RenderTree
udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)

print(udo)

for pre, fill, node in RenderTree(udo):
    print("%s%s" % (pre, node.name))

root = udo
#from anytree.dotexport import RenderTreeGraph
#RenderTreeGraph(root).to_picture()

#DOC
#http://anytree.readthedocs.io/en/latest/api.html

