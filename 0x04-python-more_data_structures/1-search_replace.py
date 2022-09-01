def search_replace(my_list, search, replace):
    if my_list is not None:
        new = []
        for i in range(0, len(my_list)):
            if my_list[i] != search:
                new.append(my_list[i])
            elif my_list[i] == search:
                new.append(replace)
        return new
