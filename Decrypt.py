__author__ = 'RiteshReddy'
from Base_Crypt import Base_Crypt
import random
class Decrypt(Base_Crypt):

    def __init__(self, seed, block_size, cipher_key, num_blocks):
        self.seed = seed
        self.cipher_key = cipher_key
        self.block_size = block_size
        self.num_blocks = num_blocks

    def decrypt(self, cipher):
        #unsubstituted = self.cieser_shift(cipher, self.cipher_key, 'L')
        permuted = self.__permute(cipher)
        message = self.unpadd_message(permuted)
        return message

    def __permute(self, cipher):
        message, n = self.split_message(cipher, self.block_size)
        perms = self.get_permutations(self.num_blocks, self.seed)
        chunks = [""] * self.num_blocks
        message_ind = 0
        for perm in perms:
            for ind, val in enumerate(perm):
                if message_ind >= len(message):
                    break
                if val == '1':
                    if message_ind % 2 == 0:
                        chunks[ind]  = self.cieser_shift(message[message_ind], random.randrange(1, self.cipher_key), 'R')
                    else:
                         chunks[ind]  = self.cieser_shift(message[message_ind], random.randrange(1, self.cipher_key), 'L')

                    #chunks[ind] = message[message_ind]
                    message_ind += 1
        return ''.join(chunks)




