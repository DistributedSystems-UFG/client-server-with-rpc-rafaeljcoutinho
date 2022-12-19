import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_search(self, value):
      position = -1
      for i in range(0, len(self.value)):
          if(self.value[i] == value):
              position = i;
              break
          return position

  def exposed_remove(self, position):
      if(position == 0):
          self.value = self.value[position+1:]
      elif(position == len(self.value)-1):
          self.value = self.value[:-1]
      else:
          self.value = self.value[:position] + self.value[position+1:]

  def exposed_sort(self):
      self.value.sort()

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value

  def exposed_insert(self, position, value):
      self.value = self.value[:position] + [value] + self.value[position:]

  def exposed_get(self, position):
      return self.value[position]

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()
