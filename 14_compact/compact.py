def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    filtered_iterator = filter(None, lst)
    filtered_list = list(filtered_iterator)
    print(filtered_list)
