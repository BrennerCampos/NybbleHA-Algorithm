
# COMP 596 - Cryptography
# Assignment 5, Programming NybbleHA algorithm
# by Brenner Campos


# Our chosen Initialization Vector and Plaintext Message
IV = "D"
message = "B345AD1F"


def main ():

    # Sets up our seed (IV), turning it into padded binary
    IV_Binary = bin(int(IV, 16))
    IV_Length = 4
    IV_Padded = IV_Binary[2:].zfill(IV_Length)
    print("IV: "+IV+"               -   Binary: "+IV_Padded)

    # Sets up our message (m), turning it into padded binary
    message_Binary = bin(int(message, 16))
    message_Length = len(message_Binary)
    message_Padded = message_Binary[0:].zfill(message_Length)[2:message_Length]


    print("Message: "+message+"   -   Binary: "+message_Padded)
    print()


    tag = merkle_damgard(IV_Padded, message_Padded)
    print("Final tag (4-bits):  \'", hex(tag)[2:].upper(), "\'")



def merkle_damgard(IV, message):
    # print("Merkle-Damgard")


    IV_Iso = hex(int(("0b"+IV),2))[2:]
    print(IV_Iso)


    block_bits = 8


    for i in range(len(message)//(block_bits)):
        block = message[i*8:(i+1)*8]
        print("Block: "+block)

        if i == 0:
            H_i = (int(IV, 2))
        elif i >0:
            if tag != 0 & tag != 1:
                H_i = H
            else:
                H_i = int(IV, 2)

        print("H_i:",H_i)

        H = davies_meyer(block, H_i, i)
 
        tag = H
        print()

    return tag


def davies_meyer(m, H, i):
    # print("Davies-Meyer")

    # print("m: ",m)
    # print("H: ",H)

    m_Iso = ("0x"+hex(int(("0b" + m), 2))[2:])
    print("Block in hex: ",m_Iso)

    H_Iso = H
    # print(H_Iso)

    m_0 = m[0:4]
    m_1 = m[4:len(m)]

    # Converting from binary to decimal
    bin1 = int(bin(int(m_Iso,16)),2)
    bin2 = H_Iso


    hex_result = hex(bin1%bin2)

    if H != 1:
        dec_result = bin1 % bin2
    else:
        dec_result = int(IV, 16)


    h = (dec_result^bin2)
    return h



main()