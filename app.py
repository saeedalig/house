from flask import Flask
from housing.logger import logging
import sys
from housing.execption import HousingException



app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        raise Exception('We are testing custom Exception')
    except Exception as e:
        housing = HousingException(e, sys)      # creating obj of HousingException
        logging.info(housing.error_message)
        logging.info('We are testing logging module!')
    return 'ML Project!'
    

if __name__ == '__main__':
    app.run(debug=True)
