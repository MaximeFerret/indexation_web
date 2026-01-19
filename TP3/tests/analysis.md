# Test queries

## 1. "chocolate" — Single keyword
- Relevant and expected results  
- High scores due to frequency, title match, and reviews
-> Search engine works well for simple queries

## 2. "chocolate brazil" — Keyword + origin
- Same result set returned  
- "brazil" adds little signal  
- Lower scores  
-> Origin is weakly discriminative in ranking

## 3. "made in usa" — Origin with synonym
- US-made products correctly retrieved  
- Works thanks to synonym expansion and indexed `origin` field  
-> Query expansion validated

## 4. "classic leather sneakers" — Descriptive query
- Product variants correctly surfaced  
- High scores (exact title match, strong BM25, reviews)  
-> Very good behavior for multi-word queries

## 5. "italian shoes" — Rare word + category
- Relevant shoe products returned  
- "italian" has limited impact  
-> Frequent terms dominate without semantic enrichment

## 6. "chocolat" — Misspelled word
- "chocolate" products still found  
- Due to token dominance and simple tokenization  
-> Uncontrolled tolerance, no true spell correction

## 7. "organic olive oil from italy" — Long query
- No results returned   
-> Doesn't work