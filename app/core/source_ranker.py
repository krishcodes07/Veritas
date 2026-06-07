from urllib.parse import urlparse
import csv


class SourceRanker:

    def __init__(self):
        self.domains = {}
        self.categories = {}

        with open("app/data/source_categories.csv") as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.categories[row["category"]] = int(row["score"])

        with open("app/data/domain_rankings.csv") as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.domains[row["domain"]] = row["category"]

    def score(self, url: str):

        domain = urlparse(url).netloc.replace("www.", "")

        category = self.domains.get(domain, "unknown")

        score = self.categories.get(category, 3)

        return {
            "domain": domain,
            "category": category,
            "score": score
        }