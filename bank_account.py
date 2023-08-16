def solution(queries):
    # Nested function to create a new account
    def CREATE_ACCOUNT(timestamp, account_id):
        if account_id in account_info:
            return "false"  # Account ID already exists
        account_info[account_id] = 0  # Initialize account balance to 0
        return "true"  # Account created successfully

    # Nested function to deposit funds into an account
    def DEPOSIT(timestamp, account_id, amount):
        if account_id not in account_info:
            return ""  # Account doesn't exist
        account_info[account_id] += int(amount)  # Add deposited amount to account balance
        return str(account_info[account_id])  # Return updated balance

    # Nested function to make a payment from an account
    def PAY(timestamp, account_id, amount):
        if account_id not in account_info:
            return ""  # Account doesn't exist
        if account_info[account_id] < int(amount):
            return ""  # Insufficient balance for payment
        account_info[account_id] -= int(amount)  # Deduct payment amount from account balance
        return str(account_info[account_id])  # Return updated balance

    account_info = {}  # Dictionary to store account information (account_id: balance)
    results = []  # List to store results of each query

    # Process each query in the list
    for query in queries:
        query_type = query[0]  # Extract query type
        timestamp = query[1]  # Extract timestamp
        account_id = query[2]  # Extract account ID

        # Determine the query type and perform corresponding operation
        if query_type == "CREATE_ACCOUNT":
            result = CREATE_ACCOUNT(timestamp, account_id)
        elif query_type == "DEPOSIT":
            amount = query[3]
            result = DEPOSIT(timestamp, account_id, amount)
        elif query_type == "PAY":
            amount = query[3]
            result = PAY(timestamp, account_id, amount)

        results.append(result)  # Add the result to the results list

    return results  # Return the list of results

# Sample list of queries
queries = [
    ["CREATE_ACCOUNT", "2023-08-15", "123"],
    ["DEPOSIT", "2023-08-16", "123", "100"],
    ["PAY", "2023-08-17", "123", "50"]
]

# Call the solution function with the sample queries
print(solution(queries))  # Output: ['true', '100', '50']
