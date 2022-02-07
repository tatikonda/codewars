def longest_consec(strarr, k):
  if k <= 0 or len(strarr) == 0 or k > len(strarr):
    return ''
  result = ''
  
  for i in range(len(strarr) - k + 1):
    sub_str = ''.join(strarr[i:i+k])
    if len(result) < len(sub_str):
      result = sub_str
  
  return result

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
