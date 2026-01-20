# Index TP2

---

## How to use:

Run the program:
```bash
python main.py
```

Run the test:
```bash
python tests/test_indexes.py
```
The test consits to check if the generated feature indexes match exactly with the expected feature indexes json.

---

## Index structure:

For `title` and `description`, a positional inverted index is also created.
```bash
{token: {url: [positions]}}
```

### `title_index.json`
Key: a normalized token
Value: a dictionnary with:
&emsp; - key: product URL
&emsp; - value: list of positions where the token appears in the title
Example:
```bash
"shoe": {
    "https://web-scraing.dev/product/8: [1]
}
```


### `description_index.json`
This index has the same structure as the title index, but is built from the `description` field.  

Note: As we can see in the test output, the description index differs from the provided expected file because token positions depend on the exact content of the website. Since the expected index was generated earlier, small changes in descriptions can lead to shifted positions.

### `brand_index.json`
Key: normalized brand name
Value: list of product URLs associated with this brand

Example:
```bash
"outdoorgear": [
    "https://web-scraping.dev/product/7",
    "https://web-scraping.dev/product/19"
]
```
Note the order of URLs is not guaranteed. For this reason, sorting is applied during testing.

### `origin_index.json`
This index is built from the `made in` field.
Key: origin
Value: list of product URLs

Example:
```bash
{
  "italy": [
    "https://web-scraping.dev/product/11",
    "https://web-scraping.dev/product/11?variant=black40"
  ]
}
```

### `reviews_index.json`
Key: product URL
Value: dictionnary with:
&emsp; - Key: "total_reviews", Value: the product total reviews
&emsp; - Key: "mean_mark", Value: the product mean mark
&emsp; - Key: "last_rating", Value: the product last rating

Example:
```bash
{
    "https://web-scraping.dev/products": {
        "total_reviews": 0,
        "mean_mark": 0,
        "last_rating": 0
    }
}
```

