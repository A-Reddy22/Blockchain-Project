import hashlib
import json
from time import time



class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.current_transactions=[]
    
    def new_block(self):
        #creates a new block and add it to the chain
        pass

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
        pass

    @property
    def last_both(self):
        #returns the last block in the chain
        pass