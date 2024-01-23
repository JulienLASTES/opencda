# -------------- DOCUMENTATION --------------

# cda.matrix:

# iMatrix (integer matrix):
  A 2d matrix of integers (+/-)

  operations:

  # Adding an integer
  adding, will add to each number in the matrix

  exemple:
  "iMatrix(...) + n"
  will do:
    iMatrix(...)[0][0] += n
    iMatrix(...)[0][1] += n
    iMatrix(...)[0][2] += n
    iMatrix(...)[...][...] += n

  # Adding a same size/smaller matrix
  addding will add matrixes together

  exemple:
  "iMatrix1 + iMatrix2"
  will do:
    iMatrix1[0][0] += iMatrix2[0][0]
    iMatrix1[0][1] += iMatrix2[0][1]
    iMatrix1[...][...] += iMatrix2[...][...]

  # Modulo
  modulo will execute the modulo operation on each of the numbers in the matrix

  exemple:
  "iMatrix(...) % n"
  will do:
    iMatrix(...)[0][0] %= n
    iMatrix(...)[0][1] %= n
    iMatrix(...)[...][...] %= n
