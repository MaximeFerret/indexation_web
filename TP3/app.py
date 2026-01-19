import streamlit as st
from search_engine.search import search

st.set_page_config(
    page_title="Mini Search Engine",
    layout="wide"
)

st.title("Mini Search Engine for E-commerce")

query = st.text_input(
    "Search a product",
    placeholder="Ex: Hiking boots"
)

if query:
    with st.spinner("Search in progress..."):
        results = search(query)

        st.subheader(
            f"Results ({len(results['results'])} products found)"
        )

        for result in results["results"]:
            with st.container():
                st.markdown(f"### [{result['title']}]({result['url']})")
                st.write(result["description"])
                st.write(f"**Score** : {result['score']}")
                st.write(
                    f"⭐ {result['metadata']['reviews'].get('mean_mark', 0)} "
                    f"({result['metadata']['reviews'].get('total_reviews', 0)} avis)"
                )
                st.divider()