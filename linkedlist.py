
class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values is not None:
           for v in values:
               self.add_after_queue(v)
            # a completer

    def __repr__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.value))
            current = current.next
        return " -> ".join(result)

    def add_before_head(self, value):
        cell = ListNode(value)
        cell.next=self.head
        self.head=cell


    def add_after_queue(self, value):
        cell=ListNode(value)
        if self.head is None:
            self.head=cell

        else:
            a=self.head
            while a.next is not None:
                a=a.next
            a.next=cell




    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return "valeur présente dans la liste : ",current.value
            current = current.next
        return("valeur non presente dans la liste")




    def insert(self, value, pos):
        # insère une nouvelle cellule contenant l'élément donné
        # à la position donnée (la tête est à 0)
        # si la position est plus grande que la longueur de la liste,
        # l'élément est inséré à la fin
        i=0
        cell=ListNode(value)
        a=self.head
        if pos==0:
            self.add_before_head(value)
        while i<pos-1:
                print(pos,i)
                i=i+1
                a=a.next
        if a is not None:
            cell.next=a.next
            a.next=cell
        else:
            self.add_after_queue(value)

    def delete(self, value):
        # deletes the first cell containing the given value
        # returns the deleted cell if an element was deleted
        pass

    def merge(self, other):
        # adds the other linked list at the end of the current list
        # the other list should be emptied after the operation
        pass

    def revert(self):
        # revert the content of the current linked list
        pass


    def afficher_liste(self):
        if self.head is None:
           return("Liste vide")
        a=self.head

        while a is not None:
              print(str(a), end=" ")
              a=a.next
        print("")


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

def main():
    l1 = LinkedList()

    l1.add_before_head(5)

    l1.add_before_head(6)
    l1.add_before_head(7)

    l1.add_before_head(8)
    l1.add_after_queue(14)
    l1.add_after_queue(13)
    l1.add_after_queue(12)
    l1.insert(26,1)
    a=l1.find(15)


    print("Liste l1:", l1)
    print(a)

if __name__ == '__main__':
    main()