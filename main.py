from llm_extractor import llm_extraction
from scraper import web_scraper, get_link_page
import streamlit as st

def main():
    st.title("Data Extraction with LLM")

    site = st.text_input("Site Link")

    # schema = {
    #     "properties": {
    #         "item_title": {"type": "string"},
    #         "item_price": {"type": "number"},
    #         "description": {"type": "string"},
    #     },
    #     "required": ["item_title", "price"],
    # }

    schema_option = ["product", "price", "description"]
    schema_field = st.multiselect("Schemas", schema_option)

    schema = {}  



    if schema_field:
        # Implement the "properties" dictionary 
        schema["properties"] = {field: {"type": "string"} for field in schema_field}

   
        if st.button("Get Data"):
            output = web_scraper(site)
            extraction_chain = llm_extraction(schema)
            processed_output = extraction_chain.run(output)
            if processed_output is not None:
                st.write("## Extracted Data")
                st.write(processed_output)



if __name__ == "__main__":
    main()