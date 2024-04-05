class FlatIterator:

    def __init__(self, list_of_list):
        self.list_items = list_of_list
        

    def __iter__(self):
        self.list_len = len(self.list_items)
        return self

    def __next__(self):
        for i in range(self.list_len):
            for j in range(len(self.list_items[i])):
                return self.list_items[i][j]

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    # test_1()
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    
    for item in FlatIterator(list_of_lists_1):
        print(item)
                
        