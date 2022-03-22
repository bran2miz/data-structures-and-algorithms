def hashmap_left_join(left_hash, right_hash):
    hash_list = []

    for key in left_hash:
        hash_list.append(key)
        hash_list.append(left_hash[key])

        if key in right_hash:
            hash_list.append(right_hash[key])
        else:
            hash_list.append(None)
    return hash_list
