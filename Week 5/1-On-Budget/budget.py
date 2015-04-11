def on_budget(books, budget):
    
    result = {
        "books_on_budget": 0,
        "loan": 0
        }

    counter = 0
    total_price = sum(books)
    books = sorted(books)

    for book in books:
        if budget - book < 0:
            break

        budget -= book
        total_price -= book
        counter += 1

    result["books_on_budget"] = counter
    result["loan"] = max(0, total_price - budget)

    return result