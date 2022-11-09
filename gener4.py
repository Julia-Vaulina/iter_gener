from collections.abc import Iterable
import types

def flat_generator(items: Iterable):
    for item in items:
        if type(item) != type('str') and isinstance(item, Iterable):
            yield from flat_generator(item)
        else:
            yield item
            

            
def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    items = [[0, 1, 2], 3, 4, [[5], [6, 7]], [[[8]], 'Fff'], 9, 'fff']
    print(test_4())
    print(list(flat_generator(items)))
