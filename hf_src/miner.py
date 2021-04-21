import time
from hashlib import sha3_512


MAX_NONCE = 1000000000000000


def SHA3512(text):
    return sha3_512(text.encode('utf-8')).hexdigest()


def mine(block_number, last_block_hash, current_txs_hash, ts,
         transactions, difficulty):
    prefix_str = '0' * difficulty
    for nonce in range(MAX_NONCE):
        text = str(block_number) + last_block_hash + \
            current_txs_hash + str(ts) + str(nonce) + transactions
        new_hash = SHA3512(text)
        if new_hash.startswith(prefix_str):
            print("Yay! Successfully mined:")
            return new_hash, nonce

    raise BaseException(
        f"Couldn't find correct has after trying {MAX_NONCE} times")


if __name__ == '__main__':
    transactions = '''
    [Gustavo -> Eduardo] $20,
    [Janete -> Julio] $45
    '''
    block_number = 0
    last_block_hash = "0x" + ("0" * 128)
    current_txs_hash = SHA3512(transactions)
    difficulty = 6  # try changing this to higher number and you will see it
    # will take more time for mining as difficulty increases
    ts = time.time()
    print("start mining")
    new_hash, nonce = mine(block_number, last_block_hash,
                           current_txs_hash, ts, transactions, difficulty)
    total_time = str((time.time() - ts))
    print(f"end mining. Mining took: {total_time} seconds")
    print()
    print("       Block Number: " + str(block_number))
    print("Previous block hash: " + last_block_hash[2:].upper())
    print("  Transactions hash: " + current_txs_hash.upper())
    print("          Timestamp: " + str(ts))
    print("              Nonce: " + str(nonce))
    print()
    print("       Transactions: " + transactions)
    print("         Block hash: " + new_hash)
    print()
