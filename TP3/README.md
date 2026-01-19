# Search engine TP3  
---

## How to use:  

Install the packages:
```bash
pip install -r requirements.txt
```

Run the program:  
```bash
python main.py "<your query>"
```  

Run the user interface:  
```bash
streamlit run app.py
```

Run the tests: 
```bash
python3 -m tests.run_tests
```
---

## My choices

### Separation between `loader.py` and `persistence.py`
The `loader.py` file is used only for generic data loading functions such as JSON and JSONL.  
The `persistence.py` file is dedicated to loading the internal search engine structures, like inverted indexes. This separation follows the single responsibility principle, improves reusability of the loader, and clearly distinguishes raw data loading from index structure loading.

### Conditional application of AND filtering
The search process first applies OR filtering, and AND filtering is only used if it returns a non-empty result set. This approach avoids empty result pages, improves user experience, and reflects pragmatic behavior found in real search engines.

### Query expansion limited to specific fields
Synonym-based query expansion is applied mainly to origin-related tokens rather than all query terms. This limits noise, avoids overly broad semantic associations, and keeps the system behavior easy to explain.

### Different weighting for title and description
The title field is given a higher weight than the description in the scoring function.  
Titles are generally more descriptive and intentional, which is standard practice in information retrieval and improves precision for short queries. The choice of weights was arbitrary.

### Explicit linear score combination
A simple weighted linear combination is used to compute the final score, without any learned model. This ensures transparency, makes tuning easier, and clearly shows the contribution of each feature. No scoring model was required by the assignment.

### Integration of customer reviews into ranking
The ranking incorporates both the average rating and the total number of reviews.  
These signals reflect perceived product quality and align with common e-commerce practices, improving ranking when textual relevance is similar.  
Customer reviews were only suggested.

### Implicit tolerance to spelling errors
No explicit spell-checking mechanism is implemented. Partial matches are still returned due to dominant tokens, allowing observation of the system’s natural tolerance and its limitations.

### Simple handling of long queries
Long queries are processed using strict filtering on non-stopword tokens, without progressive relaxation. This keeps the implementation simple and clearly highlights the limitations of a Boolean retrieval model.

### Automatic generation of test results
A test script automatically generates a `test_results.json` file, keeping a clear separation between data and results. This ensures reproducibility, supports qualitative analysis, and mirrors real evaluation workflows.

### Weights of linear score
The weightings were chosen arbitrarily but consistently in order to illustrate the relative impact of the different signals. Automatic optimisation of these weights would be a natural way to improve the system.
