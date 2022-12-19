import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print (conn.root.exposed_value())
  conn.root.exposed_append(5)       # Call an exposed operation,
  conn.root.exposed_append(6)       # and append two elements
  conn.root.exposed_append(2)
  conn.root.exposed_append(23)
  conn.root.exposed_append(54)



  print ("lista atual:")
  print ([conn.root.exposed_value()])

  conn.root.exposed_sort()

  print("lista ordenada:")
  print([conn.root.exposed_value()])

  conn.root.exposed_remove(2)
  conn.root.exposed_remove(2)

  print("lista atual, com remocoes '2' '2':")
  print([conn.root.exposed_value()])

  conn.root.exposed_insert(2,55)

  print("lista atual, com insercao '55' '2':")
  print([conn.root.exposed_value()])
