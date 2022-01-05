# from django.test import TestCase

# Create your tests here.
class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None

head = LinkNode("h")
second = LinkNode("e")
third = LinkNode("l")
fourth = LinkNode("l")
fifth = LinkNode("o")
tail = LinkNode(None)
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = tail

tmp = head
while tmp.next:
    print(tmp.val)
    tmp = tmp.next

