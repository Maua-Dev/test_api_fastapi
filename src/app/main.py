from datetime import datetime
from fastapi import FastAPI, HTTPException
from mangum import Mangum

app = FastAPI()

current_balance = 1000.0
all_transactions = [
            {
                "type" : "deposit",
                "value" : 100.0,
                "current_balance": "1000.0",
                "timestamp" : 1690482853890
            },
]

@app.get("/")
def read_root():
    global current_balance
    return {
        "name": "Vitor Soller",
        "agency": "7777",
        "account": "69420-7",
        "current_balance": current_balance
    }


@app.get("/history")
def get_history():
    global all_transactions
    return {
        'all_transactions' : all_transactions
    }

@app.post("/withdraw")
def withdraw(request: dict):
    notas200 = request.get("200", 0)
    notas100 = request.get("100", 0)
    notas50 = request.get("50", 0)
    notas20 = request.get("20", 0)
    notas10 = request.get("10", 0)
    notas5 = request.get("5", 0)
    notas2 = request.get("2", 0)

    value = (notas200 * 200) + (notas100 * 100) + (notas50 * 50) + (notas20 * 20) + (notas10 * 10) + (notas5 * 5) + (notas2 * 2)

    global current_balance
    current_balance = current_balance - value 
    timestamp = datetime.now().timestamp() * 1000
    
    response = {
        "type": "withdraw",
        "timestamp": timestamp, #milliseconds
        "current_balance": current_balance,
        "value": value
    }

    global all_transactions
    all_transactions.append(response)
    return response
    
@app.post("/deposit")
def deposit(request: dict):
    notas200 = request.get("200")
    notas100 = request.get("100")
    notas50 = request.get("50")
    notas20 = request.get("20")
    notas10 = request.get("10")
    notas5 = request.get("5")
    notas2 = request.get("2")

    value = (notas200 * 200) + (notas100 * 100) + (notas50 * 50) + (notas20 * 20) + (notas10 * 10) + (notas5 * 5) + (notas2 * 2)

    global current_balance
    current_balance = current_balance + value

    global all_transactions
    timestamp = datetime.now().timestamp() * 1000
    response = {
        "type": "deposit",
        "current_balance": current_balance,
        "timestamp": timestamp, #milliseconds
        "value": value
    }
    all_transactions.append(response)
    return response

handler = Mangum(app, lifespan="off")
