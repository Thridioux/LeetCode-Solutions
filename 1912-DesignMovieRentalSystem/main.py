from typing import List
from collections import defaultdict
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.prices = {} # (shop, movie) -> price
        self.unrented = defaultdict(set) # movie -> set of (price, shop)
        self.rented = set() # set of (price, shop, movie)
        
        for shop, movie, price in entries:
            self.unrented[movie].add((price, shop))
            self.prices[(shop, movie)] = price
        
        

    def search(self, movie: int) -> List[int]:
        if movie not in self.unrented:
            return []
        
        available_copies = sorted(list(self.unrented[movie]))
        result_shop = []
        for price, shop in available_copies[:5]:
            result_shop.append(shop)
        return result_shop
        
    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.unrented[movie].remove((price, shop))
        self.rented.add((price, shop, movie))
        

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.unrented[movie].add((price, shop))
        

    def report(self) -> List[List[int]]:
        cheapest_rented = sorted(list(self.rented))
        result_report = []
        for price, shop, movie in cheapest_rented[:5]:
            result_report.append([shop, movie])
        
        return result_report
    
    
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()