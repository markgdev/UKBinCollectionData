#!/usr/bin/env python3

# This script pulls (in one hit) the data from
# Warick District Council Bins Data
from bs4 import BeautifulSoup
from get_bin_data import AbstractGetBinDataClass


# import the wonderful Beautiful Soup and the URL grabber
class CouncilClass(AbstractGetBinDataClass):
    """
    Concrete classes have to implement all abstract operations of the
    base class. They can also override some operations with a default
    implementation.
    """

    def parse_data(self, page: str) -> dict:
        # Make a BS4 object
        soup = BeautifulSoup(page.text, features="html.parser")
        soup.prettify()

        data = {"bins": []}

        for bins in soup.select('div[class*="service-item"]'):
            bin_type = bins.div.h3.text.strip()
            binCollection = bins.select("div > p")[1].get_text(strip=True)
            # binImage = "https://myaccount.stockport.gov.uk"   bins.img['src']
            if binCollection:
                data[bin_type] = binCollection

        return data
