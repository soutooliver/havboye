
def start():
    response=send_at_get_resp("AT+CGNSINF")
    print("Ulstein TOF2 Bøye nr1 "+response)
    file=open("Innhenttest.csv","a")
    file.write(str(response)+",")
    file.flush()
    file.close()
    
