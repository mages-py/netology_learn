class FlatIterator:

    def __init__(self, list_of_list):
        self.list_items = list_of_list


    def __iter__(self):
        self.list_len = len(self.list_items)
        self.list_index = 0
        self.item_index = -1
        self.normalise_list = []
        return self
    
    def _get_normalise_list(self, data:list):
        
        for item in data:
            if not isinstance(item, list):
                self.normalise_list.append(item)
            else:
                self._get_normalise_list(item)
                                
    def __next__(self):
        if not self.normalise_list:
            self._get_normalise_list(self.list_items[self.list_index])
        if self.item_index + 1 == len(self.normalise_list):
            self.list_index += 1
            self.item_index = -1
            if self.list_index == self.list_len:
                raise StopIteration
            else:
                self.normalise_list.clear()
                self._get_normalise_list(self.list_items[self.list_index])
        self.item_index += 1
        return self.normalise_list[self.item_index]
 
 
def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
