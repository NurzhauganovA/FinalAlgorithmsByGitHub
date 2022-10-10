from block_user_node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node is None:
            self.head = new_node
            return
        while cur_node.get_next() is not None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def show_list(self):
        cur_node = self.head
        output = ''
        while cur_node is not None:
            output += "\n" + str(cur_node.get_data()) + "\n"
            cur_node = cur_node.get_next()
        print(output)
