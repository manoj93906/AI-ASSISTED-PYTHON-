def discount(price, category):
    """
    Calculate discounted price based on category and price threshold.
    
    Args:
        price: Original price
        category: Customer category ("student" or other)
    
    Returns:
        Discounted price
    """
    if category == "student":
        # Students get 10% off for prices over 1000, 5% off otherwise
        discount_rate = 0.9 if price > 1000 else 0.95
        return price * discount_rate
    
    # Non-students get 15% off for prices over 2000, no discount otherwise
    if price > 2000:
        return price * 0.85
    
    return price
