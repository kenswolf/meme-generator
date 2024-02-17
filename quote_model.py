"""Quote Class, of data related to a quote"""

class QuoteModel:
    """Quote Class, of data related to a quote"""
    def __init__(self,body:str,author:str):
        self.body = body
        self.author = author

    def __str__(self):
        return f"Author is {self.author} and quote is... {self.body}"
