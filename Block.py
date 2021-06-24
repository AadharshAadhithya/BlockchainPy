import datetime
import hashlib
import json


from config import GENISIS_HASH,GENISIS_DATA,GENISIS_DIFFICULTY,GENISIS_NONCE , GENISIS_PREV_HASH , mine_rate


class Block:

  def __init__(self,data,previous_hash,nonce,difficulty,hash,timestamp):

    self.data=data
    self.previous_hash=previous_hash
    self.nonce=nonce
    self.difficulty=difficulty
    self.hash=hash
    self.timestamp=timestamp

  def __str__(self):
    a={'hash':self.hash}
    return json.dumps({
        'timestamp': str(self.timestamp),
        'data':self.data,
        'hash':self.hash,
        'previous hash':self.previous_hash,
        'nonce':self.nonce,
        'difficulty':self.difficulty
    })

  @classmethod
  def genisis(cls,minerate):
    genisis = Block(GENISIS_DATA,GENISIS_PREV_HASH,GENISIS_NONCE,GENISIS_DIFFICULTY,GENISIS_HASH,datetime.datetime.now())
    mine_rate=minerate
    return genisis


  @classmethod
  def mineBlock(cls,prevBlock,data):

    nonce=0
    found= False;

    while not found:
      nonce=nonce+1
      timestamp=datetime.datetime.now()

      difficulty=Block.setDifficulty(prevBlock,timestamp)
      if (difficulty<1):
        difficulty =1

      stringified_block = str(timestamp)+prevBlock.hash+str(difficulty)+str(data)+str(nonce)
      hashed = hashlib.sha256(stringified_block.encode()).hexdigest()

      if (hashed[0:difficulty ] == "0"*difficulty):
        found= True;
        return Block(data=data,previous_hash=prevBlock.hash , nonce = nonce ,difficulty=difficulty,hash=hashed,timestamp=timestamp)
        
        
        

    
  @classmethod
  def  setDifficulty(cls,block,timestamp):

    difficulty=block.difficulty
    if (difficulty<1):
      return 1
    if  ( ( timestamp - block.timestamp).seconds > mine_rate):
      return difficulty-1
    else:
      return difficulty+1


  def jsonifyBlock(self):
    return  {
        'timestamp': str(self.timestamp),
        'data':self.data,
        'hash':self.hash,
        'previous hash':self.previous_hash,
        'nonce':self.nonce,
        'difficulty':self.difficulty
    }