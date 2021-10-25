print ('hello world')


from flask import Flask 
app = Flask('app')

@app.route('/')
def hello_world():
        return 'hello World'

app.run(host='0.0.0.0', post=8080)


//loop
 for i in range(5):
     print ('A number:', i)


//factorial

def factorial(n):
    if n == 0;
        return 1
        else:
            return n * factorial(n - 1)
        print(factorial(5))

//Hello world

print('hello world')


//input
 name = input('what is your name?\n')
 print('Hi, %s.' % name)

 