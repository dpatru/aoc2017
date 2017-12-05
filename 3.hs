
steps :: Int -> Int
steps cell = l + o
  where l = level cell
        o = offset cell
        level = ceil $ 0.5 * ceil $ sqrt cell - 1
        offset = abs $ -1 + rem ((2*l+1)^2 - cell) 2*l