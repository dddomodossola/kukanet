import win32pipe, win32file

#http://stackoverflow.com/questions/13319679/createnamedpipe-in-python
#https://msdn.microsoft.com/en-us/library/windows/desktop/aa365150(v=vs.85).aspx

"""
this script opens a named pipe and waits that another process opens and writes into it (as for a standard file) flushing the buffer
each written message gets read and printed here

f = open(r'\\.\pipe\comlib','a')
f.write("asd")
f.flush()
f.close()

"""

p = win32pipe.CreateNamedPipe(r'\\.\pipe\kukanet',
    win32pipe.PIPE_ACCESS_DUPLEX,
    win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT,
    1, 65536, 65536,300,None)

win32pipe.ConnectNamedPipe(p, None)

#data = b"Hello Pipe"  
#win32file.WriteFile(p, data)

while True:
    data = win32file.ReadFile(p, 4096)
    print(data)