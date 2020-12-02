from flask import Flask, json

api = Flask (__name__)

@api.route('/test1', methods=['GET'])
def get_test():
    return "Hello!"

@api.route('/test2', methods=['GET'])
def get_test2():
    return "Labais!"

if __name__ == '__main__':
    api.run()