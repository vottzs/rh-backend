from flask import Flask, jsonify, request, send_file

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

HIRING_STAGES = [
  'Applied',
  'Contacted',
  'Interview',
  'Interview Done',
  'Offer Draft',
  'Offered',
  'Offer Accepted',
  'Offer Declined',
  'Hired'
]

@app.route('/hiring_stages', methods=['GET'])
def get_hiring_stages():
    response_object = {'status': 'success'}
    response_object['hiring_stages'] = HIRING_STAGES
    response = jsonify(response_object)
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5001")
