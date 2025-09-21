from typing import List
from collections import defaultdict
import heapq

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.prices = {} # (shop, movie) -> price
        self.unrented = defaultdict(list) # movie -> min heap of (price, shop)
        self.rented = [] # min heap of (price, shop, movie)
        self.unrented_set = defaultdict(set) # movie -> set of (price, shop) for O(1) removal check
        self.rented_set = set() # set of (price, shop, movie) for O(1) removal check
        
        for shop, movie, price in entries:
            heapq.heappush(self.unrented[movie], (price, shop))
            self.unrented_set[movie].add((price, shop))
            self.prices[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        if movie not in self.unrented:
            return []
        
        # Clean up the heap by removing rented items from the top
        while self.unrented[movie] and self.unrented[movie][0] not in self.unrented_set[movie]:
            heapq.heappop(self.unrented[movie])
        
        result = []
        temp_removed = []
        seen_shops = set()  # Track shops we've already added to avoid duplicates
        
        # Get up to 5 cheapest available copies
        while len(result) < 5 and self.unrented[movie]:
            price, shop = heapq.heappop(self.unrented[movie])
            if (price, shop) in self.unrented_set[movie]:
                if shop not in seen_shops:  # Only add if we haven't seen this shop
                    result.append(shop)
                    seen_shops.add(shop)
                temp_removed.append((price, shop))
            # If not in set, it was rented, so we skip it
        
        # Put back the items we temporarily removed
        for item in temp_removed:
            heapq.heappush(self.unrented[movie], item)
            
        return result

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.unrented_set[movie].discard((price, shop))
        heapq.heappush(self.rented, (price, shop, movie))
        self.rented_set.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.rented_set.discard((price, shop, movie))
        heapq.heappush(self.unrented[movie], (price, shop))
        self.unrented_set[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        # Clean up the heap by removing dropped items from the top
        while self.rented and self.rented[0] not in self.rented_set:
            heapq.heappop(self.rented)
        
        result = []
        temp_removed = []
        seen_shop_movie = set()  # Track (shop, movie) pairs we've already added
        
        # Get up to 5 cheapest rented movies
        while len(result) < 5 and self.rented:
            price, shop, movie = heapq.heappop(self.rented)
            if (price, shop, movie) in self.rented_set:
                if (shop, movie) not in seen_shop_movie:  # Only add if we haven't seen this (shop, movie) pair
                    result.append([shop, movie])
                    seen_shop_movie.add((shop, movie))
                temp_removed.append((price, shop, movie))
            # If not in set, it was dropped, so we skip it
        
        # Put back the items we temporarily removed
        for item in temp_removed:
            heapq.heappush(self.rented, item)
            
        return result
    
    
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()