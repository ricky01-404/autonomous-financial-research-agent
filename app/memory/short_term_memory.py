class ShortTermMemory:

    def __init__(self):

        self.memory = []

    def add(self, item):

        self.memory.append(item)

        # Keep only recent 5 interactions
        self.memory = self.memory[-5:]

    def get_memory(self):

        return self.memory