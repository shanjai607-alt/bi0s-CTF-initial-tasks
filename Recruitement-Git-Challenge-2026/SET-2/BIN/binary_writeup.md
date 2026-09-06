# Binary Exploitation Write-up

## Flag

bi0s{w3lc0me_t0_0v3rfl0w1ng_buff3rs}

## Method

1. I checked the binary using:
   file bof

2. It showed that `bof` is a Linux x86-64 executable.

3. Since I was using a Mac, I ran it inside an Ubuntu Docker container.

4. I ran the program using:
   ./bof

5. The program asked for a payload.

6. I tested a long input using:
   python3 -c 'print("A"*65)' | ./bof

7. This showed that the challenge was related to a buffer overflow.

8. After analysing the binary, I obtained the flag.

## Conclusion

The challenge demonstrates a basic buffer overflow vulnerability.

Flag:
bi0s{w3lc0me_t0_0v3rfl0w1ng_buff3rs}