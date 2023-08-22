# Function that adds the respective value to each individual
def calculate_employment_score(emp_length):
    if emp_length < 1.9:
        return 100
    elif 2 <= emp_length < 4.9:
        return 125
    elif 5 <= emp_length < 6.9:
        return 150
    elif 7 <= emp_length < 9.9:
        return 175
    elif emp_length >= 10:
        return 200
    return 0

def calculate_homeownership_score(homeownership):
    if homeownership == "RENT":
        return 100
    elif homeownership == "MORTGAGE":
        return 150
    elif homeownership == "OWN":
        return 200
    return 0

def calculate_annual_income_score(annual_income):
    if 10_000 <= annual_income < 25_000:
        return 100
    elif 25_000 <= annual_income < 49_999:
        return 150
    elif 50_000 <= annual_income < 74_999:
        return 175
    elif 75_000 <= annual_income < 99_999:
        return 200
    elif annual_income >= 100_000:
        return 225
    return 0

def calculate_credit_line_score(earliest_credit_line):
    if earliest_credit_line < 1999:
        return 200
    elif 2000 <= earliest_credit_line < 2005:
        return 175
    elif 2005 <= earliest_credit_line < 2010:
        return 150
    elif 2010 <= earliest_credit_line < 2015:
        return 125
    return 0

def calculate_credit_utilized_score(credit_utilized_percent):
    if credit_utilized_percent < 25:
        return 175
    elif 26 <= credit_utilized_percent < 50:
        return 125
    elif credit_utilized_percent > 50:
        return 75
    return 0

def check_verified(income_verified):
    if income_verified == "Not Verified":
        return 100
    return 0
    
def employment_to_homeownership(employment, homeownership):
    if employment < 2 and homeownership in ["RENT", "MORTGAGE"]:
        return 100
    return 0

def low_income_high_usage(income, usage):
    if usage > 80:
        return 100
    elif income < 25000 and usage > 36:
        return 100
    return 0

def calculate_credit_score(row):
    emp_score = calculate_employment_score(row["emp_length"])
    homeownership_score = calculate_homeownership_score(row["homeownership"])
    income_score = calculate_annual_income_score(row["annual_income"])
    credit_line_score = calculate_credit_line_score(row["earliest_credit_line"])
    verified = check_verified(row["verified_income"])
    homeownership_employment = employment_to_homeownership(row["emp_length"], row["homeownership"])
    
    credit_utilized_percent = 0
    total_credit_limit = row["total_credit_limit"]
    if total_credit_limit == 0:
        credit_utilized_score = 0
    else:
        credit_utilized_percent = (row["total_credit_utilized"] / total_credit_limit) * 100
        credit_utilized_score = calculate_credit_utilized_score(credit_utilized_percent)

    income_usage = low_income_high_usage(row["annual_income"], credit_utilized_percent)
    total_score = emp_score + homeownership_score + income_score + credit_line_score + credit_utilized_score - (verified + homeownership_employment + income_usage)
    return total_score

def calculate_credit_to_utilized(row):
    total_credit_limit = 0
    percentage = 0
    total_credit_limit = row["total_credit_limit"]
    if total_credit_limit == 0:
        credit_utilized_score = 0
    else:
        percentage = (row["total_credit_utilized"] / total_credit_limit) * 100
    return percentage

def calculate_risk_score(row):
    def calculate_delinq_2y_score(delinq_2y):
        if delinq_2y == 0:
            return 0
        elif 2 <= delinq_2y <= 4:
            return 3.1 * 1.2
        elif delinq_2y >= 5:
            return 6.3 * 1.5
        return 0

    def calculate_inquiries_last_12m_score(inquiries_last_12m):
        if inquiries_last_12m == 0:
            return 0
        elif 4 <= inquiries_last_12m <= 7:
            return 3.1
        elif inquiries_last_12m >= 8:
            return 6.3 * 1.5
        return 0

    def calculate_open_credit_lines(open_credit_lines):
        if 4 <= open_credit_lines <= 7:
            return 3.1 * 1.2
        elif open_credit_lines > 8:
            return 6.3 * 1.5
        return 0

    def calculate_collections_12m(collections_12m):
        if 1 <= collections_12m <= 3:
            return 3.1
        elif collections_12m > 4:
            return 6.3 * 1.5
        return 0

    def calculate_historical_failed_to_pay(historical):
        if 2 <= historical < 3:
            return 3.1
        elif historical > 3:
            return 6.3 * 1.5
        return 0

    def calculate_collections_amount_ever(colecction):
        if 500 <= colecction <= 1500:
            return 3.1
        elif colecction > 1501:
            return 6.3
        return 0

    def calculate_installment_acc(installment):
        if 2 <= installment < 3:
            return 3.1 * 1.2
        elif installment > 3:
            return 6.3 * 1.5
        return 0

    def calculate_accounts_opened(accounts):
        if 2 <= accounts < 5:
            return 3.1 * 1.2
        elif accounts > 6:
            return 6.3 * 1.5
        return 0

    def months_since_last_credit_inquiry(inquiery):
        if 4 <= inquiery <= 9:
            return 3.1
        elif inquiery > 10:
            return 6.3
        return 0

    def accounts_120d_past_due(accounts):
        if 2 <= accounts < 3:
            return 3.1
        elif accounts > 3:
            return 6.3 * 1.5
        return 0

    def calculate_accounts_past_due_30d(accounts):
        if 2 <= accounts <= 3:
            return 3.1 * 1.2
        elif accounts > 4:
            return 6.3 * 1.5
        return 0

    def calculate_open_cc_accounts(accounts):
        if 2 <= accounts <= 6:
            return 3.1 * 1.2
        elif accounts > 7:
            return 6.3 * 1.5
        return 0

    def calculate_cc_with_balance(accounts):
        if 2 <= accounts < 5:
            return 3.1 * 1.2
        elif accounts > 6:
            return 6.3 * 1.5
        return 0

    def calculate_mortgage_acc(accounts):
        if 2 <= accounts < 3:
            return 3.1
        elif accounts > 3:
            return 6.3 * 1.5
        return 0

    def calculate_tax_liens(liens):
        if 2 <= liens < 3:
            return 3.1 * 1.2
        elif liens > 3:
            return 6.3 * 1.5
        return 0
        
    def calculate_acc_never_delinq(account):
        if 80 <= account <= 90:
            return 3.1
        elif account < 80:
            return 6.3
        return 0

    risk_score = (
        calculate_delinq_2y_score(row["delinq_2y"])
        + calculate_inquiries_last_12m_score(row["inquiries_last_12m"])
        + calculate_open_credit_lines(row["open_credit_lines"])
        + calculate_collections_12m(row["num_collections_last_12m"])
        + calculate_historical_failed_to_pay(row["num_historical_failed_to_pay"])
        + calculate_collections_amount_ever(row["total_collection_amount_ever"])
        + calculate_installment_acc(row["current_installment_accounts"])
        + calculate_accounts_opened(row["accounts_opened_24m"])
        + months_since_last_credit_inquiry(row["months_since_last_credit_inquiry"])
        + accounts_120d_past_due(row["num_accounts_120d_past_due"])
        + calculate_accounts_past_due_30d(row["num_accounts_30d_past_due"])
        + calculate_open_cc_accounts(row["num_open_cc_accounts"])
        + calculate_cc_with_balance(row["num_cc_carrying_balance"])
        + calculate_mortgage_acc(row["num_mort_accounts"])
        + calculate_tax_liens(row["tax_liens"])
        + calculate_acc_never_delinq(row["account_never_delinq_percent"])


    )

    return risk_score

