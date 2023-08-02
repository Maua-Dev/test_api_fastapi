from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

current_balance = 1000.0

@app.get("/")
def read_root():
    global current_balance
    return {
        "name": "Luigi Trevisan",
        "agency": "0000",
        "account": "00000-0",
        "current_balance": current_balance
    }


@app.get("/history")
def get_history():
    return {
        'all_transactions' : [
            {
                "type" : "deposit",
                "value" : 100.0,
                "timestamp" : 1690482853890
            },
            {
                "type" : "withdraw",
                "value" : 200.0,
                "timestamp" : 1690482853890
            }
        ]
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

    global current_balance
    current_balance = current_balance - (notas200 * 200) - (notas100 * 100) - (notas50 * 50) - (notas20 * 20) - (notas10 * 10) - (notas5 * 5) - (notas2 * 2)

    return {
        "current_balance": current_balance,
        "timestamp": 1690482853890, #milliseconds
    }
    
@app.post("/deposit")
def deposit(request: dict):
    notas200 = request.get("200")
    notas100 = request.get("100")
    notas50 = request.get("50")
    notas20 = request.get("20")
    notas10 = request.get("10")
    notas5 = request.get("5")
    notas2 = request.get("2")

    global current_balance
    current_balance = current_balance + (notas200 * 200) + (notas100 * 100) + (notas50 * 50) + (notas20 * 20) + (notas10 * 10) + (notas5 * 5) + (notas2 * 2)
    return {
        "current_balance": current_balance,
        "timestamp": 1690482853890, #milliseconds
    }

handler = Mangum(app, lifespan="off")
