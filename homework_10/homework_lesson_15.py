import requests
import json
import random


def sort_by_surname(item: dict) -> str:
    surname = item["quoteAuthor"].split()[-1]
    return surname


class Quotes:
    def __init__(self, quotes_count: int, filename: str, file_format: str = "json"):
        self.filename = f"{filename}.{file_format}"
        self.format = file_format
        self.quotes_count = quotes_count
        self._url = "http://api.forismatic.com/api/1.0/"
        self._quotes = []

    @property
    def url(self):
        return self._url

    @property
    def quotes(self):
        return self._quotes

    def get_quotes(self):
        for quote_num in range(self.quotes_count):
            self._quotes += [self.get_quote()]

    def get_quote(self):
        params = {
            "method": "getQuote",
            "format": self.format,
            "key": random.randint(0, 999999),
            "lang": "en"
        }
        response = requests.get(self._url, params=params)
        try:
            if response.json()["quoteAuthor"].strip() == "":
                return self.get_quote()
            else:
                return response.json()
        except json.decoder.JSONDecodeError:
            return self.get_quote()

    def print_quotes(self):
        for quote in self._quotes:
            quote_text = quote["quoteText"].strip()
            quote_author = quote["quoteAuthor"].strip()
            print(f"\"{quote_text}\" - {quote_author}.")

    def save_quotes(self):
        with open(self.filename, "w") as json_file:
            json.dump(sorted(self._quotes, key=sort_by_surname), json_file)


# Usage:
# if __name__ == "__main__":
    # quotes_count = 100
    # filename = "test"
    # file_format = "json"
    # test = Quotes(quotes_count=quotes_count, filename=filename, file_format=file_format)
    # test.get_quotes()
    # test.print_quotes()
    # test.save_quotes()
