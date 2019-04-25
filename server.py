from main import *
lastUpdateID=None
print ('firing up\n')
while True:
    updates=getUpdates(lastUpdateID)
    if len(updates["result"])>0:
        lastUpdateID=getLatestUpdateID(updates) + 1
        for update in updates["result"]:
            message,who,name=extract(update)
            try:
                print("from",name,"message",message)
            except:
                pass 
            if message=="/start":
                reply="Hello, "+name+". I'm Poetu Clem, the writer in ACAA. You can check his writings here ❄️(send clem) and you can also get some geek jokes🤡(send geek). 😃"
            else:
                reply=process(message,who)
            sendMessage(reply,who)
            print(reply, "reply sent")    

       
