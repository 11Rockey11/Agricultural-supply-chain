import hashlib
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('./supplychain-ip-firebase-adminsdk-vbfs3-853264b00e.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'transaction').document(u'test1')
class Block:
  def __init__(self,buyerName,sellerName,previousHash,productName,productID,buyerID,sellerID,descofProd,quality):
    self.buyerName = buyerName
    self.sellerName = sellerName
    self.previousHash = previousHash
    self.productName = productName
    self.productID = productID
    self.buyerID = buyerID
    self.sellerID = sellerID
    self.descofProd = descofProd
    self.quality = quality
    self.timeStamp = datetime.datetime.now()
    self.hashValue = self.hash()
  def hash(self):
    value = str(self.buyerID)+str(self.sellerID)+str(self.productID)+str(self.previousHash)+str(self.quality)+str(self.timeStamp)
    result = hashlib.sha256(value.encode())
    return result.hexdigest()

class Chain:
  def __init__(self):
    self.blocks = []
  def genesis(self):
    gen = Block("0","0",None,"0",None,None,None,"0","0")
    self.blocks.append(gen)
  def addBlock(self):
    block = Block("Hariharan",self.blocks[-1].buyerName,None,"Carrot",12121,"A543",self.blocks[-1].sellerID,"Fresh product","Good")
    self.blocks.append(block)
    doc_ref.set({
      u'sellerName': block.sellerName,
      u'sellerID': block.sellerID,
      u'buyerName': block.buyerName,
      u'buyerID': block.buyerID,
      u'previousHash': block.previousHash,
      u'productName': block.productName,
      u'productID': block.productID,
      u'descofProd': block.descofProd,
      u'quality': block.quality,
      u'timeStamp': block.timeStamp,
      u'hashValue': block.hashValue
    })

  def printChain(self):
    for block in self.blocks:
      print(block.sellerID," ",block.hashValue," ",block.sellerName)
  
def main():
  C = Chain()
  C.genesis()
  C.addBlock()
  C.printChain()
  
main()
