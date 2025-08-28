import hashlib
import json
from time import time



class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.current_transactions=[]
    
    def new_block(self, proof, previous_hash=None):
        #creates a new block and add it to the chain
        """ param proof: is an int, the proof given by the Proof of Work Algorithm
        :param previous_hash:hash of previous block
        :return<dict> New Block"""

    def new_transaction(self,sender,reciepent,amount):
        #adds a new transaction to the list of transactions
        """
        Creates a new transaction to go into the next mined Block
        :param sender:<str> Address of the sender
        :param recipent: Address of the recipient
        :param amount: int- amount
        :return: int value. The index of the block that will hold this transaction
        """
        self.current_transactions.append({
            'sender':sender,
            'recipient':reciepent,
            'amount':amount,
        })

        return self.last_block['index']+1


    @staticmethod
    def hash(block):
        #hashesh a block
        """
        Creates a SHA-256 hash of a block
        :param block:<dict> Block
        returns 256 bit string
        """
        block_string=json.dumps(block,sort_keys=True).encode()
        return

    @property
    def last_both(self):
        #returns the last block in the chain
        pass

    def proof_of_work(self,last_proof):
        """ 
        A Proof of Work algorithm (PoW) is how new Blocks are created or mined on the blockchain. 
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         -
        """

        proof=0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof
    
    @staticmethod