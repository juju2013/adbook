#! /usr/bin/env python

import os,email

class adbook:
    def __init__(self):
        self.contacts={}
    
    def add(self, addrs):
        try:
            for a in addrs.split('\n\t'):
                name, addr=email.utils.parseaddr(a)
                self.contacts[name]=addr
        except: pass

def main():
    ab = adbook()
    i = 0
    for (path, dirs, files) in os.walk('path_to_maildir'):
        for f in files:
            with open(os.path.join(path, f),encoding='ISO-8859-1') as m:
                x=email.message_from_file(m)
                ab.add(x['from'])
                ab.add(x['to'])
                ab.add(x['cc'])
                i+=1
                if i%500==0:
                    print("%i(%i)..."%(i, len(ab.contacts)))
    o = open('pine.adbook.txt','w')
    for k in ab.contacts:
        print("%s\t%s"%(k, ab.contacts[k]))
        o.write("%s\t%s\t%s\n"%(k, k, ab.contacts[k]))
    o.close()
        
if __name__ == "__main__":
    main()

