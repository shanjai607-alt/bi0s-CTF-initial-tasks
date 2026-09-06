# Reverse Engineering Writeup

## Challenge

The given Python program takes a flag as input and transforms it before comparing it with a predefined array.

## Analysis

The program performs the following operations:

1. The input is Base64 encoded.
2. The encoded string is split into two parts.
3. The first part is XORed with the values in the x array.
4. The second part is XORed using the same key values in a cyclic manner.
5. The resulting values are compared with the given arr array.

Since XOR is reversible:

A ^ B ^ B = A

I reversed the XOR operations and obtained the Base64 encoded string:

Ymkwc3t5MHVfYXIzX24wd180X3IzdjNyczNfM25nMW4zM3J9

Finally, I Base64 decoded the result.

## Flag

bi0s{y0u_ar3_n0w_4_r3v3rs3_3ng1n33r}