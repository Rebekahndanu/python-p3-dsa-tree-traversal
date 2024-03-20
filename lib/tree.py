class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        if not self.root:
            return None

        queue = [self.root]
        front = 0

        while front < len(queue):
            node = queue[front]
            front += 1

            if node.get('id') == id:
                return node

            for child in node.get('children', []):
                queue.append(child)

        return None