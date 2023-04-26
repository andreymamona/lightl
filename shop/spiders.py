import scrapy


class OmaSpider(scrapy.Spider):
    name = "oma.by"
    allowed_domains = ["www.oma.by"]
    start_urls = ["https://www.oma.by/osveshchenie-c"]
    current_page = 0

    def parse(self, response, **kwargs):
        self.current_page += 1
        for product in response.css(".catalog-grid .product-item"):
            data = {
                "external_id": product.attrib.get("data-ga-product-id").strip(),
                "name": product.attrib.get("data-ga-product-name").strip(),
                "price": product.attrib.get("data-ga-product-price").strip(),
                "category": product.attrib.get("data-ga-category-last").strip(),
                "link": f"{self.allowed_domains[0]}{product.css('a.area-link::attr(href)').get()}",
                "image_name": f"https://www.oma.by{product.css('.catlg_list_img::attr(data-src)').get()}"}
            yield data

        next_page = response.css(".page-nav_box .btn__page-nav:last-child::attr(href)").get()
        if next_page is not None:
            if self.current_page >= 5:
                return
            yield response.follow(next_page, callback=self.parse)

