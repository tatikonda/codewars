def count_smileys(arr):
    smileys = []
    for s in arr:
        if len(s) == 2 and s[0] in [":", ";"] and s[-1] in [")", "D"]:
            smileys.append(s)
        elif len(s) > 2 and s[0] in [":", ";"] and s[1] in ["-", "~"] and s[-1] in [")", "D"]:
            smileys.append(s)
    return len(smileys)

def count_smileys(arr):
    total = 0
    if not arr:
      return 0
    smileys =  [':)', ';)', ':~)', ';~)', ':-)', ';-)', ':D', ';D', ':~D', ';~D', ':-D', ';-D']
    for i in arr:
      if i in smileys:
        total += 1
    return total

print(count_smileys([':D',':~)',';~D',':)']))