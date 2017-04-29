from twitter import Twitter,OAuth

%OAuth Details replace ID1,ID2,ID3,ID4
tw = Twitter(auth = OAuth(ID1,ID2,ID3,ID4))
print tw
tw.statuses.update(status = "Hello World!!")
print tw
