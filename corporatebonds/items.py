# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class BondItem(Item):
    url = Field()
    
    """
    # define the fields for your item here like:
    state   = Field()
    start   = Field()
    end     = Field()
    """
