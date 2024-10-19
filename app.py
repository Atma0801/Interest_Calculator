from flask import Flask, render_template, request

app = Flask(__name__)

# Define bank classes here
class BankofIndia:
    def __init__(self, principal, time, interest_rate):
        self.principal = principal
        self.time = time
        self.interest_rate = interest_rate

    def amount_repayable(self):
        total = self.principal + (self.principal * self.interest_rate * self.time) / 100
        return total

class StateBankofIndia:
    def __init__(self, principal, time, interest_rate):
        self.principal = principal
        self.time = time
        self.interest_rate = interest_rate

    def amount_repayable(self):
        total = self.principal + (self.principal * self.interest_rate * self.time) / 100
        return total

class Icici:
    def __init__(self, principal, time, interest_rate):
        self.principal = principal
        self.time = time
        self.interest_rate = interest_rate

    def amount_repayable(self):
        total = self.principal + (self.principal * self.interest_rate * self.time) / 100
        return total

class CentralBankofIndia:
    def __init__(self, principal, time, interest_rate):
        self.principal = principal
        self.time = time
        self.interest_rate = interest_rate

    def amount_repayable(self):
        total = self.principal + (self.principal * self.interest_rate * self.time) / 100
        return total

# Route definition
@app.route('/', methods=['GET', 'POST'])
def index():
    total = None
    
    if request.method == 'POST':
        try:
            principal = float(request.form['principal'])
            time = float(request.form['time'])
            rate = float(request.form['rate'])
            bank_name = request.form['bank']

            # Create bank object based on user input
            if bank_name == 'BankofIndia':
                bank = BankofIndia(principal, time, rate)
            elif bank_name == 'StateBankofIndia':
                bank = StateBankofIndia(principal, time, rate)
            elif bank_name == 'Icici':
                bank = Icici(principal, time, rate)
            elif bank_name == 'CentralBankofIndia':
                bank = CentralBankofIndia(principal, time, rate)
            else:
               
                bank = None

            if bank:
                total = bank.amount_repayable()
            else:
                total = f"Loan calculated for bank: {bank_name}, Total Amount Repayable: ₹{(principal + (principal * rate * time) / 100):.2f}"
        
        except ValueError:
            total = "Invalid input! Please enter valid numbers."

    return render_template('index.html', total=total)

if __name__ == "__main__":
    app.run(debug=True)
