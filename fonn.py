class livros:
  def __init__(self, title, version, author, publisher, isbn):
    self.title = title
    self.author = author
    self.publisher = publisher
    self.isbn = isbn
    self.disponibility = True
    self.version = version
    #futuro = date.fromordinal(hj.toordinal()+45)
    self.borrowT = 0

  def checkDisp(self):
    if self.disponibility == True:
      return True
    else:
      return False



  def borrow(self, devTime):
    today = date.today()
    if self.disponibility == True:
      self.disponibility = False
      self.borrowT += int(devTime)
      return 'Book must be returned within %d days'%self.borrowT
    else:
      return 'Book is unavailable; it will be available within %d days'%self.borrowT

  def unborrow(self):
    if self.disponibility == True:
      return 'Book is already available'
    else:
      self.disponibility = True
      return 'Book is now available'

  def updateBook(self,version,publisher):
    self.version = int(version)
    self.publisher = publisher

def download(arq):
  f = open(arq,"r")
  l = f.read()
  f.close()
  l = l.split("\n")
  obj = []
  for i in range(0,len(l)):
    l[i] = l[i].split(":")
  for i in l:
       obj.append(livros("%s"%i[0],"%s"%i[1],"%s"%i[2],"%s"%i[3],"%s"%i[4]))

  for i in obj:
      print(i.title)
download("mclivi")

