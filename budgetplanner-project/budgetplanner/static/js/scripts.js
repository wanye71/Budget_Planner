document.addEventListener("DOMContentLoaded", function() {
    let totalBudgetForecast = 0;
    let totalBudgetAmount = 0;
    document.querySelectorAll("[data-budget-forecast]").forEach(function(row) {
        const budgetForecastElement = row.querySelector('.budget-forecast');
        const budgetAmountElement = row.querySelector('.budget-amount');
        
        const budgetForecast = parseFloat(row.getAttribute("data-budget-forecast")) || 0;
        const budgetAmount = parseFloat(row.getAttribute("data-budget-amount")) || 0;
        
        totalBudgetForecast += budgetForecast;
        totalBudgetAmount += budgetAmount;
        
        if (budgetAmount > budgetForecast) {
            budgetForecastElement.style.color = 'red';
        }
    });
    document.getElementById("total-budget-forecast").innerText = totalBudgetForecast.toFixed(2);
    document.getElementById("total-budget-amount").innerText = totalBudgetAmount.toFixed(2);
});