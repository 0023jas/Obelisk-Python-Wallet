# ee9715b9221fd260146e7562dd5fa389fc70f984eac4a0aee22b0f6372384109
"""
import binascii
from bip_utils import Bip39EntropyGenerator, Bip39MnemonicGenerator, Bip39WordsNum

# Generate a random mnemonic string of 15 words
# mnemonic = Bip39MnemonicGenerator.FromWordsNumber(Bip39WordsNum.WORDS_NUM_15)

# Generate the mnemonic string from entropy bytes:
entropy_bytes_hex = b"00000000000000000000000000000000"
mnemonic = Bip39MnemonicGenerator.FromEntropy(binascii.unhexlify(entropy_bytes_hex))
print(mnemonic)
"""
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

# Generate random mnemonic
#mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)
mnemonic = "pony rule fabric donor this exclude duck kingdom olympic rookie ozone civil"
print("Mnemonic string: %s" % mnemonic)
# Generate seed from mnemonic
seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

# Generate BIP44 master keys
bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
# Print master key
print("Master key (bytes): %s" % bip_obj_mst.PrivateKey().Raw().ToHex())
print("Master key (extended): %s" % bip_obj_mst.PrivateKey().ToExtended())
print("Master key (WIF): %s" % bip_obj_mst.PrivateKey().ToWif())

# Generate BIP44 account keys: m/44'/0'/0'
bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
# Generate BIP44 chain keys: m/44'/0'/0'/0
bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)

# Generate the address pool (first 20 addresses): m/44'/0'/0'/0/i
for i in range(5):
    bip_obj_addr = bip_obj_chain.AddressIndex(i)
    print("%d. Address public key (extended): %s" % (i, bip_obj_addr.PublicKey().ToExtended()))
    print("%d. Address private key (extended): %s" % (i, bip_obj_addr.PrivateKey().Raw().ToHex()))
    print("%d. Address: %s" % (i, bip_obj_addr.PublicKey().ToAddress()))