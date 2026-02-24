""" Daily Challenge : Pagination
Instructions: Pagination System
Goal:
Create a Pagination class that simulates a basic pagination system. """

import math

class Pagination:
    def __init__(self, items = None, page_size = 10):
        if items is not None:
            self.items = items
        else:
            self.items = []

        self.page_size = page_size
        self.current_idx = 0

        number_of_items = len(self.items) # Divide by page size to know how many pages are needed
        raw_page_count = number_of_items / self.page_size # Round UP to the next whole number
        total_pages = math.ceil(raw_page_count) # Store the result
        self.total_pages = total_pages

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end] #slice the list