#task1
n=int(input('please enter your number: '))

def fibonacci(n):
    if n<=0:
        print('you have to enter a positive number')
    elif n ==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print('your fibonacci number is: ',fibonacci(n))#



#task3
    
users = {}

def register_user(username):
    if username in users:
        print('Username ' +' ' + str(username) +' '+ 'already exists')
    else:
        users[username] = []
        print('User'+' ' +str(username) + ' ' +'registered successfully.')

def send_message(sender, receiver, message):
    if sender not in users:
        print('Sender does not exists')
    elif receiver not in users:
        print('receiver does not exists')
    else:
        msg = {"sender": sender, "receiver": receiver, "text": message}
        users[sender].append(msg)
        users[receiver].append(msg)
        print('Message from '+' '+str(sender)+' '+ 'to' +' '+ str(receiver) +' '+'sent successfully')

def view_messages(username):
    if username not in users:
        print("User is not registered.")
    else:
        messages = users[username]
        if not messages:
            print('No messages')
        else:
            for msg in messages:
                if msg['sender'] == username:
                    print('Message sent to'+' ' + msg['receiver']+' '+'from'+' '+msg['text'])
                else:
                    print('Message received from'+' ' + msg['sender']+' '+ msg['text'])
register_user("Malak")
register_user("Mariam")
send_message("Malak", "Mariam", "Hello, Mariam!")
view_messages("Mariam")
send_message("Mariam", "Malak", "Hi, Malak!")
view_messages("Malak")
