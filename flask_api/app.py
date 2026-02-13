from flask import Flask, jsonify, request

from file_name import get_pretty_names

app = Flask(__name__)

@app.route('/pretty-names', methods=['POST'])
def pretty_names_endpoint():
    try:
        data = request.json or {}
        
        folder_path = data.get('folder_path')
        split_char = data.get('split_char')
        chars_to_remove = data.get('chars_to_remove')
        remove_after_char = data.get('remove_after_char')
        
        if not folder_path:
            return jsonify({"error": "folder_path is required"}), 400
        if split_char is None:
            return jsonify({"error": "split_char is required"}), 400
        
        get_pretty_names(folder_path, split_char, chars_to_remove, remove_after_char)
        return jsonify({"message": "File names processed successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/test', methods=['GET'])
def test_endpoint():
    return "Test Page!"

@app.route('/')
def home():
    return "Welcome to the Pretty Names API!"

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)