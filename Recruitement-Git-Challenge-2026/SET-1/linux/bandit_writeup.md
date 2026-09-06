# Bandit Writeup

## Level 0 → Level 1

Command used:

    ls
    cat readme

Explanation:
`ls` lists the files in the directory.
`cat readme` displays the contents of the readme file, which contains the password for Level 1.

Password:
[6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR]
## Level 1 → Level 2

Command used:

    ls
    cat ./-

Explanation:

`ls` lists the files in the current directory.

The file is named `-`. Normally `cat -` treats `-` as standard input, so
`cat ./-` is used to explicitly refer to the file named `-`.

Password:

[PK8fYLZg2hnHSz83plBL1iEPKdD3QToB]
## Level 2 → Level 3

Command used:

    ls
    cat "./--spaces in this filename--"

Explanation:

`ls` lists the files in the current directory.

The filename contains spaces and begins and ends with `--`.
The `./` specifies that the file is in the current directory, while
the quotes make the shell treat the entire filename as one argument.

The `cat` command displays the contents of the file, which contains
the password for Level 3.

Password:

[7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME]

## Level 3 → Level 4

Command used:

    ls
    cd inhere
    ls -la
    cat ./...Hiding-From-You

Explanation:

`ls` lists the files and directories in the current directory.

`cd inhere` moves into the `inhere` directory.

`ls -la` lists all files, including hidden files, along with detailed information.

The file `...Hiding-From-You` is hidden because its name starts with dots.

`cat ./...Hiding-From-You` displays the contents of the file.
The `./` tells Linux that the file is located in the current directory.

Password:

[xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq]

## Level 4 → Level 5

Commands used:

    ls
    cd inhere
    ls
    file ./*
    cat ./-fileXX

Explanation:

`ls` lists the files and directories in the current directory.

`cd inhere` moves into the `inhere` directory.

`file ./*` checks the type of every file in the directory.
It is used to identify which file contains human-readable text.

The file identified as ASCII text contains the password.

`cat ./-fileXX` displays the contents of that file.
The `./` is used because the filename begins with `-`, which could otherwise be interpreted as an option.

Password:

[## Level 4 → Level 5

Commands used:

    ls
    cd inhere
    ls
    file ./*
    cat ./-fileXX

Explanation:

`ls` lists the files and directories in the current directory.

`cd inhere` moves into the `inhere` directory.

`file ./*` checks the type of every file in the directory.
It is used to identify which file contains human-readable text.

The file identified as ASCII text contains the password.

`cat ./-fileXX` displays the contents of that file.
The `./` is used because the filename begins with `-`, which could otherwise be interpreted as an option.

Password:

[6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG]

## Level 5 → Level 6

Commands used:

    ls
    cd inhere
    find . -type f -size 1033c ! -executable
    cat ./maybehere07/.file2

Explanation:

`ls` lists the files and directories.

`cd inhere` moves into the `inhere` directory.

`find . -type f -size 1033c ! -executable` searches for a regular file that is exactly 1033 bytes and is not executable.

The command found the required file:
`./maybehere07/.file2`

`cat ./maybehere07/.file2` displays the contents of the file, which contains the password for Level 6.

Password:

[## Level 5 → Level 6

Commands used:

    ls
    cd inhere
    find . -type f -size 1033c ! -executable
    cat ./maybehere07/.file2

Explanation:

`ls` lists the files and directories.

`cd inhere` moves into the `inhere` directory.

`find . -type f -size 1033c ! -executable` searches for a regular file that is exactly 1033 bytes and is not executable.

The command found the required file:
`./maybehere07/.file2`

`cat ./maybehere07/.file2` displays the contents of the file, which contains the password for Level 6.

Password:

[pXa26xhMWaC2SvDotA4r9EgZkulOeSBW]

## Level 6 → Level 7

Command used:

    find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
    cat /path/to/file

Explanation:

`find /` searches from the root directory, so it can search the entire filesystem.

`-user bandit7` finds files owned by the user `bandit7`.

`-group bandit6` finds files owned by the group `bandit6`.

`-size 33c` finds files that are exactly 33 bytes in size.

`2>/dev/null` hides permission-denied error messages so that the useful result is easier to see.

The `find` command identifies the file containing the password.

`cat` displays the contents of the identified file.

Password:

[Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3]

## Level 7 → Level 8

Commands used:

    ls
    grep millionth data.txt

Explanation:

`ls` lists the files in the current directory.

The required file is `data.txt`.

`grep millionth data.txt` searches the file for the line containing the word `millionth`.

The password is located on the same line after the word `millionth`.

Password:

[VR1ljMayciFxbnUokuQmJFw6QC9VKtub]

## Level 8 → Level 9

Commands used:

    ls
    sort data.txt | uniq -u

Explanation:

`ls` lists the files in the current directory.

`sort data.txt` sorts all the lines in `data.txt` so identical lines are next to each other.

`uniq -u` displays only the lines that occur exactly once.

The output is the password for Level 9.

Password:

[## Level 8 → Level 9

Commands used:

    ls
    sort data.txt | uniq -u

Explanation:

`ls` lists the files in the current directory.

`sort data.txt` sorts all the lines in `data.txt` so identical lines are next to each other.

`uniq -u` displays only the lines that occur exactly once.

The output is the password for Level 9.

Password:

[EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl]

## Level 9 → Level 10

Commands used:

    ls
    strings data.txt
    strings data.txt | grep "="

Explanation:

`ls` lists the files in the current directory.

`strings data.txt` extracts readable text from the file, which also contains binary data.

`grep "="` searches the readable strings for lines containing the `=` character.

The matching line contains the password for Level 10.

Password:

[B0s2khmbT9u0geKuOoVGW3JZKhndE3BG]

## Level 10 → Level 11

Command used:

    ls
    base64 -d data.txt

Explanation:

`ls` lists the files in the current directory. It shows that `data.txt` is present.

`base64 -d data.txt` decodes the contents of `data.txt` from Base64 format. The decoded output contains the password for Level 11.

Password:

[pYfOY6HwUsDj5rL9UvyhU7MCmv8vN5Ro]













