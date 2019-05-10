import binascii

x = b'abcdefg'
x = binascii.hexlify(x)
y = str(x,'ascii')

print(x) # Outputs b'74657374' (hex encoding of "test")
print(y) # Outputs 74657374



'''
import binascii

x = b'test'
x = binascii.hexlify(x)
y = str(x,'ascii')

print(x) # Outputs b'74657374' (hex encoding of "test")
print(y) # Outputs 74657374

x_unhexed = binascii.unhexlify(x)
print(x_unhexed) # Outputs b'test'

x_ascii = str(x_unhexed,'ascii')
print(x_ascii) # Outputs test

This code contains examples for converting ASCII
characters to and from hexadecimal. In your situation,
 the line you'd want to use is str(binascii.hexlify(c),'ascii').



'''
