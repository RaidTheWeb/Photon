import requests, sys

while True:
  hashed = input('\u001b[0m[#]: Hash To Decode: ')
  hash_type = input('\u001b[0m[#]: Hash Type: ')

  email = "therealraidtheweb@gmail.com"

  code = "7cae2a01d34c7187"
  re = 'https://md5decrypt.net/en/Api/api.php?hash=%s&&hash_type=%s&&email=%s&&code=%s' % (hashed, hash_type, email, code)

  r = requests.get(re)
  print(r.text)
  print('[#]: Cracked in:', r.elapsed.total_seconds())
  while True:
    q = input('\u001b[0m[#]: Crack Another Y or N: ')
    if q.lower().startswith('y'):
      break
    if q.lower().startswith('n'):
      sys.exit(0)
