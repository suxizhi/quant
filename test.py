from ib.opt import Connection, message
import time

def my_account_handler(msg):
    print(msg)



def my_tick_handler(msg):
    print(msg)

def main():
    conn = Connection.create(port=4002, clientId=100)
    conn.registerAll(my_account_handler)
    conn.connect()

    conn.enableLogging()
    time.sleep(1) #Simply to give the program time to print messages sent from IB
    conn.disconnect()
    #conn.reqAccountUpdates()
if __name__ == "__main__": main()
