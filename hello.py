from flask import Flask

app = Flask(__name__)

health_degree = 100
guessedLuckynum = 5
stepOne =10
stepTwo=2
stepThree = 5
stepFour = 4


@app.route('/health')
def health():
    if (health_degree > 100 ):
        return '<h1>Fever</h1>'
    else:
        return '<h1>Cold</h1>'

@app.route('/luckynumber')
def luckynumber():
    print("Guess your lucky num")
    first = (guessedLuckynum*stepOne)
    second  = (first*stepTwo)
    third = (second / stepThree)
    finalOut = (third / stepFour)
    
    return  '{}'.format(finalOut)
    

if __name__ == '__main__':
    app.run(debug=True)
