def masks(exp: int) -> list[int]:
    size = 1 << exp

    init_mask = ~(~0 << size)
    size >>= 1
    init_mask >>= size
    init_mask <<= size

    res = [init_mask]

    mask = init_mask
    for i in range(1, exp):
        mask >>= size >> 1
        mask &= ~(~0 << size)
        for _ in range(i):
            mask = (mask << size) + mask
            size <<= 1
        res.append(mask)
        size >>= i + 1

    return res
