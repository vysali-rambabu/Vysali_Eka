import socket


class Sample:

    def __init__(self, name):
        self.name = name

    def result(self):
        print('Invoke result()')
        self.display('Hello', self.print_msg)

    def display(self, data, func):
        print('Invoke display()')
        data = 'Hello'

    def print_msg(data):
        print('Invoke print_msg()')
        print(data)


s = Sample('hi')
s.result()

s = '<deal>I am good.</deal></QML>'
print(s[s.index('<deal>') + 6:s.index('</deal>')])

print(socket.gethostname())