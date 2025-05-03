def main():
    # This program converts currency from one type to another
    # It uses the exchange rates from the European Central Bank
    # The exchange rates are updated daily

    print("Welcome to the Currency Converter!")
    def convert_to_pounds(euros):
        # Example conversion rate: 1 euro = 0.86 pounds
        return euros * 0.86

    def convert_to_euros(pounds):
        # Example conversion rate: 1 pound = 1.16 euros
        return pounds * 1.16

    euros = 100  # Example input value in euros
    pounds = convert_to_pounds(euros)
    print(f"{pounds} pounds is equal to {euros} euros.")

    main()