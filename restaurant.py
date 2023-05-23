class Table:
    def __init__(self, no_of_diners: int):
        self.no_of_diners = no_of_diners
        # This sets the bill to empty upon creation of the table object
        self.bill = []

    def order(self, item: str, price: float, quantity: int = 1):
        '''Add an order item to the bill of the table'''
        is_new_item = True
        index_of_existing_item = -1

        # This checks if the ordered item exists in the bill
        for i, existing_bill_item in enumerate(self.bill):
            if existing_bill_item['item'] == item and existing_bill_item['price'] == price:
                index_of_existing_item = i
                is_new_item = False

        # This adds item to the 'end' of the bill if it is a new item, and increments the quantity
        # of the existing item if it is not a new item
        if is_new_item:
            self.bill.append(
                {'item': item, 'price': price, 'quantity': quantity})
        else:
            self.bill[index_of_existing_item]['quantity'] += quantity

    def remove(self, item: str, price: float, quantity: int = 1):
        '''Remove existing item from bill'''
        is_new_item = True
        index_of_existing_item = -1

        # Checks the bill for the entered item and returns False if less of item than to be removed
        for i, existing_bill_item in enumerate(self.bill):
            if existing_bill_item['item'] == item and existing_bill_item['price'] == price:
                if existing_bill_item['quantity'] < quantity:
                    return False
                is_new_item = False
                index_of_existing_item = i

        # Returns False if the bill does not contain the item to be removed
        if is_new_item:
            return False
        # Removes quantity of item from the bill, as input by user
        else:
            self.bill[index_of_existing_item]['quantity'] -= quantity
            if self.bill[index_of_existing_item]['quantity'] == 0:
                # Removes item completely, if quantity of it is now 0
                self.bill.pop(index_of_existing_item)
            return True

    def get_subtotal(self):
        '''Return subtotal of table bill prior to addition of service charge'''
        sub_total = 0
        for i, item in enumerate(self.bill):
            sub_total += item['price'] * item['quantity']
        return sub_total

    def get_total(self, service_charge: float = 0.10):
        '''Return bill breakdown, including service charge'''
        return {
            'Sub Total': f"£{format(self.get_subtotal(), '.2f')}",
            'Service Charge': f"£{format(self.get_subtotal() * service_charge, '.2f')}",
            'Total': f"£{format(self.get_subtotal() + (self.get_subtotal() * service_charge), '.2f')}"
        }

    def split_bill(self):
        '''Return subtotal of bill before service charge, divided equally between initial diners at the table'''
        return round((self.get_subtotal() / self.no_of_diners), 2)
