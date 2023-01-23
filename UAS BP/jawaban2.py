Blok try akan menghasilkan NameError, karena x tidak ditentukan:

try:
  print(x)
except NameError:
  print("Variable x tidak ditentukan")
except:
  print("Telah terjadi kesalahan")

