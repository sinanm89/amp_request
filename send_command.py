import socket

data = {'_ask': 1, '_command': "CreateGame", "player_number": 8}

frame = bytes()

for key,val in data.iteritems():
    frame += chr(0)
    frame += chr(len(key))
    frame += bytes(key)
    frame += chr(0)
    frame += chr(len(str(val)))
    frame += bytes(val)
frame += chr(0) + chr(0)

# frame1 = b"\x00\x04"+ b"_ask" + b"\x00\x01"+ b"1" + b"\x00\x08"+ b"_command" + b"\x00\x0a"+ b"CreateGame" + b"\x00\x0d"+"player_number" + b"\x00\x01"+ b"8" + b"\x00\x00"
print frame
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',1234))
s.send(frame)
data = s.recv(1024)
print data
