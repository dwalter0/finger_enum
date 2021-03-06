# finger_enum
Brute force usernames if the finger service is on the target.

```
usage: finger_enum.py [-h] [-p PORT] [-w WORDLIST] [-O OUTFILE] host

positional arguments:
  host                  Host to connect to finger on.

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Port to connect to finger on.
  -w WORDLIST, --wordlist WORDLIST
                        Wordlist to try against finger.
  -O OUTFILE, --outfile OUTFILE
                        List of usernames go out to this file in a wordlist like format. Since it's a slow bruteforce, successes are written to file as it goes.
```

This is quite slow. It is faster to use the scanner/finger/finger_users module in msfconsole.

There are some false positives especially with double worded names or words with apostrophes but it should find the valid ones.
