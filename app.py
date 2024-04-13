# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def simple_program():
    designed_content = '''
          _______  __   __  _______    _______  __   __  _______  ______   
         |       ||  | |  ||       |  |       ||  | |  ||       ||    _ |  
         |    _  ||  | |  ||    ___|  |    ___||  |_|  ||    ___||   | ||  
         |   |_| ||  |_|  ||   |___   |   |___ |       ||   |___ |   |_||_ 
         |    ___||       ||    ___|  |    ___||_     _||    ___||    __  |
         |   |    |       ||   |___   |   |      |   |  |   |___ |   |  | |
         |___|    |_______||_______|  |___|      |___|  |_______||___|  |_|                                                                     
    '''
    return designed_content + '\n' + 'First Simple Program'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
