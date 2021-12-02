Doubly linked list is all about "Two way traversing" through the linked list.

That means, Each Node has not only DATA, NEXT but also "PREVIOUS" pointer
pointing to Previous Node.

***How you can Imagine***

+-------------------------+
| PREVIOUS | DATA | NEXT  |
+-------------------------+

Example:

+-------head-------+        +----------------+         +----------------+         +----------------+
| Null | A | NEXT  |<======>|  * | B | NEXT  |<======> |  * | C | NEXT  |<======> |  * | D | Null  |
+--p-----d---------+        +--p---d---------+         +--p---d---------+         +--p---d---------+

head.prev = Null
head.next = C

#B.prev = head
#B.next = C

# when Node B is deleted
C.prev = head
C.next = None
