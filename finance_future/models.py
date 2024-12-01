from django.db import models




# Create your models here.
class FinancialHealth(models.Model):
    name = models.CharField(max_length=100) #User's name
    income = models.DecimalField(max_digits=10, decimal_places=2) #Monthly income
    expenses = models.DecimalField(max_digits=10, decimal_places = 2) #Monthly expenses
    savings = models.DecimalField(max_digits=10, decimal_places=2) #Monthly savings
    debt = models.DecimalField(max_digits=10, decimal_places=2) #Total debt
    #created_at = models.DateTimeField(auto_now_add = True) #Date of record creation


        #we can add more field as needed

    def __str__(self):
        return f"Financial Health of {self.name}; Income: {self.income}; Expenses: {self.expenses}; Savings: {self.savings}; Debt: ${self.debt}"
    
class UserInsights(models.Model):
    user = models.OneToOneField('auth.User', on_delete= models.CASCADE)
    spending_balance = models.DecimalField(max_digits=10,decimal_places=2)
    debt_management= models.DecimalField(max_digits=10, decimal_places=2)
    savings_plan = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Insights for UserName:{self.user}; Spending: {self.spending_balance}; Debt: {self.debt_management}; Savings: {self.savings_plan}"

