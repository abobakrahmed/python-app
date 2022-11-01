from flask import Flask, jsonify,json
import MySQLdb

app = Flask(__name__)

@app.route('/api/connection-status/', methods=['GET'])
def main():
  # Connect to the MySQL database
  try:
    db = MySQLdb.connect(host = 'database-1.cop4stlsdd2l.us-east-1.rds.amazonaws.com', user = 'admin', passwd = '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', db = 'dbName', connect_timeout=5)
  # Carry out normal procedure
    print('Connection successful')
    return jsonify({'success': true,'status': 'connected'});
  except:
    # Terminate
    print('Connection unsuccessful')
    return jsonify({'success': true,'status': 'failed'})


# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=True, threaded=True, port=5000)
