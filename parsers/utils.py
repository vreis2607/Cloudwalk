import json
# Format JSON schema
def jsonify(dictionary):
    return json.dumps(dictionary, indent=4)