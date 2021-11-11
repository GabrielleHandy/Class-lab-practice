"""Classes for melon orders."""

class AbstractMelonOrder:
    def __init__(self, species, qty, country_code = "None"):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.country_code = country_code

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        
        super().__init__(species, qty)
        # self.species = species
        # self.qty = qty
        # self.shipped = False
        # self.order_type = "domestic"
    
    def get_total(self):
        """Calculate price, including tax."""
        tax = 0.08
        base_price = 5
        if self.species == "christmas":
            base_price *= 1.5
        
        total = (1 + tax) * self.qty * base_price

        return total   

    

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    
    
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        
        
        super().__init__(species, qty, country_code)
        # self.species = species
        # self.qty = qty
        self.country_code = country_code
        self.order_type = "international"
        # self.shipped = False
       
    def get_total(self):
        """Calculate price, including tax."""
        tax = 0.17
        base_price = 5
        if self.species == "christmas":
            base_price *= 1.5
        
        total = (1 + tax) * self.qty * base_price
        if self.qty < 10:
            total += 3

        return round(total, 2)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order within the US government."""
    
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        
        super().__init__(species, qty)
        # self.species = species
        # self.qty = qty
        # self.shipped = False
        self.order_type = "government"
        self.passed_inspection = False
    
    def get_total(self):
        """Calculate price, including tax."""
        tax = 0
        base_price = 5
        if self.species == "christmas":
            base_price *= 1.5
        
        total = (1 + tax) * self.qty * base_price

        return total   
    
    def mark_inspection(self, passed):
        """Record inspection results."""
        if passed == True:
            self.passed_inspection = True