#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    # Get JSON input
    data = request.get_json()

    # Read marks from JSON
    marks = data.get("marks", 0)

    # Prediction logic
    if marks >= 50:
        prediction = "Pass"
    else:
        prediction = "Fail"

    # Return JSON response
    return jsonify({
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:





# In[ ]:




