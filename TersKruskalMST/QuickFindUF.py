class QuickFindUF:
    def __init__(self, N):   
       self.id = list()
       for i in range (0, N):
           self.id.append(i)

    def find(self, p):
        return self.id[p]

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)
      
    def union(self, p, q):
       pid = self.id[p]
       qid = self.id[q]

       for i in range(0, len(self.id)):
           if self.id[i] == pid:
               self.id[i] = qid