#!/usr/bin/python3

import os
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('host', help="Host to connect to finger on.")
    parser.add_argument('-p','--port', help="Port to connect to finger on.")
    parser.add_argument('-w','--wordlist', help="Wordlist to try against finger.")
    parser.add_argument('-O','--outfile', help="List of usernames go out to this file in a wordlist like format. Since it's a slow bruteforce, successes are written to file as it goes.")
    args = parser.parse_args()
    
    wordlist = []
    found_usernames = []
    f = open(f'{args.wordlist}', "r")
    for line in f:
        wordlist.append(line.replace("\n",""))

    print(f'{len(wordlist)} usernames to check.')

    for user in wordlist:
        finger_out = subprocess.Popen(['finger',f'{user}@{args.host}'], 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT)
        finger_out.wait()
        stdout,stderr = finger_out.communicate()
        
        stdoutStr = str(stdout)

        lines = stdoutStr.split("\\n")
        for i in range (1,len(lines)):
            words = lines[i].split(" ")
            for word in words:
                if word != user and word != "???" and word.strip() != "" and word != "'": #then we've found a valid user          
                    if words[0] not in found_usernames:
                        found_usernames.append(words[0])
                        print(f'finger of \'finger {user}@{args.host}\' returned some users')
                        print(f'{words[0]}')
                        if args.outfile != "":
                            with open(args.outfile,'a') as f:
                                f.write(words[0])
                                f.write("\n")
                                f.close()      

if __name__ == "__main__":
    main()