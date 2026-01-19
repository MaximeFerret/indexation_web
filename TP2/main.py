from indexer.loader import load_jsonl
from indexer.inverted_index import create_position_index
from indexer.feature_index import create_feature_index
from indexer.review_index import create_review_index
from indexer.persistence import save_index


STOPWORDS = {
    "the", "and", "or", "a", "an", "of", "to", "in", "with", "is",
    "for", "on", "this", "that", "it", "as", "are", "be"
}


def main():
    documents = load_jsonl("input/products.jsonl")

    title_index = create_position_index(documents, "title", STOPWORDS)
    description_index = create_position_index(documents, "description", STOPWORDS)

    brand_index = create_feature_index(documents, "brand")
    origin_index = create_feature_index(documents, "made in")

    reviews_index = create_review_index(documents)

    save_index(title_index, "output/title_index.json")
    save_index(description_index, "output/description_index.json")
    save_index(brand_index, "output/brand_index.json")
    save_index(origin_index, "output/origin_index.json")
    save_index(reviews_index, "output/reviews_index.json")


if __name__ == "__main__":
    main()