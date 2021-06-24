import datetime
import hashlib
import json
from Block import Block

from config import GENISIS_HASH,GENISIS_DATA,GENISIS_DIFFICULTY,GENISIS_NONCE , GENISIS_PREV_HASH , mine_rate



class Blockchain:

  def __init__(self , minerate):
    mine_rate = minerate
    self.chain = []
    self.chain.append(Block.genisis(minerate))

  def addBlock(self,data):

    self.chain.append(Block.mineBlock(self.chain[-1] , data))
  
 
  @classmethod
  def isValidChain(cls,chain):

	    for i in range(1,len(chain)):
	      
	      blk = chain[i]
	      prev_blk = chain[i-1]

	      stringified_block = str(blk.timestamp)+blk.previous_hash +str(blk.difficulty)+str(blk.data)+str(blk.nonce)
	      hashed = hashlib.sha256(stringified_block.encode()).hexdigest()

	      if (hashed != blk.hash):
	        print("hashes do not match")
	        return False

	      if (prev_blk.hash != blk.previous_hash):
	        print("previous hashes do not match")
	        return False

	      if (abs(prev_blk.difficulty - blk.difficulty)!=1) :
	        prev_blk.difficulty - blk.difficulty
	        i
	        print("difficulties tampered")
	        return False

	    
	    return True
        
      
     


  def replaceChain(self , chain):

		  if (len(chain) > len(self.chain)):

		    if (Blockchain.isValidChain(chain)):

		      self.chain=chain;

  def jsonifyBlockchain(self):
			selfdicts=[]
			for block in self.chain:
				selfdicts.append(block.jsonifyBlock())
			return (selfdicts)
	    	