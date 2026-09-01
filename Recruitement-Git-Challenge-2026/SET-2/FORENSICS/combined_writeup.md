# Steganography Write-up

## Flag

vidyutctf{4r3_y4_w1nn1ng_s0n?}

## Method

1. I downloaded the three images given in the challenge:
   - chall.png
   - incredible.png
   - pepe.png

2. I checked the files using the `file` command.

3. The images were PNG files, so I inspected them for hidden information.

4. I checked the image contents and metadata to look for suspicious data.

5. After analysing the images, I found the hidden flag.

## Conclusion

The challenge used steganography to hide information inside the provided images.

Flag:
vidyutctf{4r3_y4_w1nn1ng_s0n?}