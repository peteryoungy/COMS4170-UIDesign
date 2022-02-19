from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 4

sales = [
	{   
        "id": 1,
		"salesperson": "James D. Halpert",
		"client": "Shake Shack",
		"reams": 100
	},
	{
        "id": 2,
		"salesperson": "Stanley Hudson",
		"client": "Toast",
		"reams": 400
	},
	{
        "id": 3,
		"salesperson": "Michael G. Scott",
		"client": "Computer Science Department",
		"reams": 1000
	},
]

clients = [
    "Shake Shack",
    "Toast",
    "Computer Science Department",
    "Teacher's College",
    "Starbucks",
    "Subsconsious",
    "Flat Top",
    "Joe's Coffee",
    "Max Caffe",
    "Nussbaum & Wu",
    "Taco Bell",
]


# ROUTES

@app.route('/')
def welcome():
   return render_template('welcome.html')   


# ajax for log_sales.js
@app.route('/infinity', methods=['GET', 'POST'])
def infinity():
    
    return render_template('log_sales.html', sales = sales, clients = clients)


# ajax for log_sales.js
@app.route('/save_sale', methods=['GET', 'POST'])
def save_sale():
    global sales
    global current_id 
    global clients

    json_data = request.get_json()   
    new_sale = json_data["new_sale"] 
    
    print(new_sale)

    # func: update sales
    new_id = current_id 
    new_sale_entry = {
        "id":  current_id,
        "salesperson": new_sale["salesperson"],
        "client": new_sale["client"],
        "reams": new_sale["reams"]
    }
    sales.insert(0, new_sale_entry)
    current_id += 1

    # func: update client
    if new_sale_entry["client"] not in clients:
        clients.append(new_sale_entry["client"])

    return jsonify(sales = sales, clients = clients)


@app.route('/delete_sale', methods=['GET', 'POST'])
def delete_sale():

    global sales
    # global current_id 
    # global clients

    json_data = request.get_json()   
    id = int(json_data["id"]) 
    
    # print(id)
    # print(type(id))

    # sales = [sales[i]["id"] != id for i in range(len(sales))]
    print(sales)

    index = 0
    for i in range(0, len(sales)):
        if sales[i]["id"] == id:
            index = i
            break
    print(index)
    sales.pop(index)

    print(sales)

    return jsonify(sales = sales)


if __name__ == '__main__':
   app.run(debug = True)




