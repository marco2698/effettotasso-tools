from flask import Blueprint, render_template, request

bp = Blueprint('budget', __name__)

@bp.route('/', methods=['GET', 'POST'])
def budget():
    result = None
    if request.method == 'POST':
        income = float(request.form['income'])
        expenses = float(request.form['expenses'])
        savings = income - expenses
        result = {
            'income': income,
            'expenses': expenses,
            'savings': savings,
            'savings_pct': round((savings / income) * 100, 2)
        }
    return render_template('budget.html', result=result)
