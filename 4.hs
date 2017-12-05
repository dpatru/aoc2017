
getLines:: IO [String]
getLines = do
  l <- getLine
  if null l
  then return []
  else do
    ls <- getLines
    return (l:ls)

processLine :: Int -> String -> Int
processLine acc line = acc + f (words line)
 where f [] = 1
       f (x:xs) | x `elem` xs = 0
                | otherwise = f xs
 
main :: IO()
main = do
  -- lines <- getLines
  contents <- getContents
  let x = foldl processLine 0 $ lines contents
  putStrLn $ "valid passphrases are " ++ show x

 