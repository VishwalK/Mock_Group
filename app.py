from flask import Flask, request, jsonify, render_template
import utils
from database import house_detail
app = Flask(__name__)

@app.route('/')
def Home():
    locality = utils.get_all_location()
    return render_template('index.html' , localities =locality) 

@app.route('/home_price_pred', methods=['POST'])
def home_price_pred():
    if request.method == 'POST':
        size = float(request.form['BHK'])
        total_sqft = float(request.form['Square Fit'])
        bath = float(request.form['Bathroom'])
        location = request.form['Location']

        location = location.lower()

        final_predicted_price = utils.prediction_price(size, total_sqft, bath, location)
        house_info = dict(size=size, total_sqft=total_sqft, bath=bath, location=location, final_predicted_price=final_predicted_price)
        house_detail.insert_one(house_info)
        # return jsonify({'size':size, 'total_sqft': total_sqft, 'bath':bath, 'location':location})
        # return jsonify({'final_predicted_price': final_predicted_price})
        return render_template('result.html', prediction = final_predicted_price)
@app.route('/location')
def get_all_location():
    return jsonify({"Locations": utils.get_all_location()})

if __name__ == "__main__":
    app.run(debug=True)