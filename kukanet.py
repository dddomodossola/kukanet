import win32pipe, win32file
import win32security
import pywintypes

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
pipename = r'\\.\pipe\kukanet'

sa = win32security.SECURITY_ATTRIBUTES()
sa.SetSecurityDescriptorDacl(1, None, 0)

p = win32pipe.CreateNamedPipe(pipename,
    win32pipe.PIPE_ACCESS_DUPLEX,
    win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT,
    win32pipe.PIPE_UNLIMITED_INSTANCES, 65536, 65536, 6000, sa)
    
win32pipe.ConnectNamedPipe(p, None)

#data = b"Hello Pipe"  
#win32file.WriteFile(p, data)

while True:
    data = win32file.ReadFile(p, 4096)
    print(data)