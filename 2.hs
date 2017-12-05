
-- -- first attempt
-- getLines:: IO [String]
-- getLines = do
--   l <- getLine
--   if null l
--   then return []
--   else do
--     ls <- getLines
--     return (l:ls)

-- processLine:: String -> Int
-- processLine s = maximum ns - minimum ns
--   where ns:: [Int]
--         ns = [read w :: Int | w <- words s]
  
-- main:: IO()
-- main = do
--   lines <- getLines
--   let s = sum [processLine l | l <- lines]
--   putStrLn $ "sum is " ++ show s

-- -- second attempt: one line at a time
-- processLines :: Int -> IO(Int)
-- processLines acc = do
--   l <- getLine
--   if null l
--   then return acc
--   else
--     let ns = [read w :: Int | w <- words l] in
--       processLines (acc + maximum ns - minimum ns)

  
-- main :: IO()
-- main = do
--   x <- processLines 0
--   putStrLn $ "Answer is " ++ show x

-- third attempt
getLines:: IO [String]
getLines = do
  l <- getLine
  if null l
  then return []
  else do
    ls <- getLines
    return (l:ls)

processLine :: Int -> String -> Int
processLine acc line = acc + maximum ns - minimum ns
 where ns = [read w :: Int | w <- words line]
 
main :: IO()
main = do
  lines <- getLines
  let x = foldl processLine 0 lines
  putStrLn $ "sum is " ++ show x

 