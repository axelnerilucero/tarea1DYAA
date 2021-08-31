class NodoArbol:
    def __init__( self, value, left=None, mid=None, right=None ):
        self.data = value
        self.left = left
        self.mid = mid
        self.right = right

head = NodoArbol(20, None, NodoArbol(19, NodoArbol(67, None, NodoArbol(99, None, None, None), None), None, None), NodoArbol(23, None, NodoArbol(57, None, None, ), None))

print(head.mid.left.mid.data)
print(head.right.mid.data)
