class Node:
    def __init__(self, data: any):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'( {self.data} )'


class LinkedList:
    def __init__(self):
        self.start = None

    def __repr__(self):
        nodes = ['START']

        for node in self:
            nodes.append(str(node.data))

        nodes.append('NIL')

        return '\n' + ' --> '.join(nodes)

    def __iter__(self):
        node = self.start

        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        length = 0

        for _ in self:
            length += 1

        return length

    def insert_at_beginning(self, element: 'Node'):
        element.next = self.start
        self.start = element

    def insert_at_end(self, element: 'Node'):
        if self.start is None:
            self.start = element
            return

        for node in self:
            last = node

        last.next = element

    def insert_after_node(self, element: 'Node', node_reference: any):
        for node in self:
            if node.data == node_reference:
                element.next = node.next
                node.next = element
                return

    def delete_node(self, element_data: any):
        if self.start is None:
            return

        if self.start.data == element_data:
            self.start = self.start.next
            return

        prev = None
        for node in self:
            if node.data == element_data:
                prev.next = node.next
                return
            prev = node

    def search(self, element_data: any):
        for node in self:
            if node.data == element_data:
                return node

        return None

    def traverse(self):
        for node in self:
            print(node.data)
