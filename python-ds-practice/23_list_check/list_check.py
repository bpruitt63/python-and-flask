def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    newlst = []
    for item in lst:
        if isinstance(item, list):
            newlst.append(True)
        else: 
            newlst.append(False)
    
    if False in newlst:
        return False
    else: 
        return True
