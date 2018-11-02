def subset_sum_brute_force(s, t, n, i):
  if n == t:
    return True
  else:
    if i == len(s):
      return False
    else:
      if subset_sum_brute_force(s, t, n + s[i], i + 1):
        return True
      elif subset_sum_brute_force(s, t, n, i + 1):
        return True
      else:
        return False

# Returning False

s = [
  10011110000,
  10000001111,
  1011001100,
  1000110011,
  110101010,
  101010101,
  10000000,
  20000000,
  1000000,
  2000000,
  100000,
  200000,
  10000,
  20000,
  1000,
  2000,
  100,
  200,
  10,
  20,
  1,
  2
]

print(subset_sum_brute_force(s, 11144444444, 0, 0))

# Returning True

s = [
  1001111000,
  1000000111,
  101100110,
  100011001,
  11010101,
  10101010,
  1000000,
  2000000,
  100000,
  200000,
  10000,
  20000,
  1000,
  2000,
  100,
  200,
  10,
  20,
  1,
  2
]

print(subset_sum_brute_force(s, 1114444444, 0, 0))
