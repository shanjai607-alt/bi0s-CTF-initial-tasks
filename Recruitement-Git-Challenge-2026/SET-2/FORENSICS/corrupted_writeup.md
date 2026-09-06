# c0rrupt3d - Writeup

## Flag

vidyutctf{4r3_y4_w1nn1ng_s0n?}

## Method

The given `flag.png` file was not recognized as a valid PNG file.

I first checked the file using the `file` command and then inspected its first bytes using `xxd`.

The PNG header was corrupted.

A valid PNG file should start with:

89 50 4e 47 0d 0a 1a 0a

I created a copy of the original file and replaced the corrupted first 8 bytes with the correct PNG header.

## Commands Used

cp flag.png flag_fixed.png

printf '\x89\x50\x4e\x47\x0d\x0a\x1a\x0a' | dd of=flag_fixed.png bs=1 count=8 conv=notrunc

file flag_fixed.png

open flag_fixed.png

After fixing the PNG header, the image opened successfully and revealed the flag.

## Conclusion

The challenge was solved by identifying the corrupted PNG header and restoring the correct PNG file signature.  