-- Insert dummy data into the transactions table
INSERT INTO public.transactions (account_id, customer_id, amount, transaction_type, description, category_id, transaction_date, status)
VALUES
    (1, 1, -50.00, 'debit', 'Groceries', 1, '2024-12-22', 'completed'),
    (2, 2, 200.00, 'credit', 'Paycheck', 2, '2024-12-21', 'completed'),
    (3, 3, -100.00, 'debit', 'Dining Out', 1, '2024-12-20', 'completed'),
    (4, 4, -20.00, 'debit', 'Parking', 3, '2024-12-19', 'pending'),
    (5, 5, -150.00, 'debit', 'Shopping', 1, '2024-12-18', 'completed'),
    (6, 6, 500.00, 'credit', 'Freelance Job', 2, '2024-12-17', 'completed'),
    (7, 7, -50.00, 'debit', 'Transport', 3, '2024-12-16', 'completed'),
    (8, 8, 300.00, 'credit', 'Paycheck', 2, '2024-12-15', 'completed'),
    (9, 9, -100.00, 'debit', 'Dining', 1, '2024-12-14', 'pending'),
    (10, 10, -75.00, 'debit', 'Parking', 3, '2024-12-13', 'completed');
