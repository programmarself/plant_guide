import streamlit as st
import pandas as pd

# Load datasets
def load_data():
    summer = pd.read_csv("datasets/summer.csv")
    winter = pd.read_csv("datasets/winter.csv")
    spring = pd.read_csv("datasets/spring.csv")
    return {
        "Summer": summer,
        "Winter": winter,
        "Spring": spring
    }

# Display plant data for a category
def display_category(data, season):
    st.subheader(f"{season} Plants")
    for _, row in data.iterrows():
        st.write(f"**{row['Name']}**: {row['Description']}")

# Search plants across categories
def search_plants(datasets, query):
    st.subheader(f"Search Results for: '{query}'")
    results_found = False
    for season, data in datasets.items():
        matches = data[data["Name"].str.contains(query, case=False, na=False)]
        if not matches.empty:
            results_found = True
            st.write(f"### {season} Plants")
            for _, row in matches.iterrows():
                st.write(f"**{row['Name']}**: {row['Description']}")
    if not results_found:
        st.write("No plants found matching your search query.")

# Main function
def main():
    st.title("Plant Guide")
    st.sidebar.title("Navigation")

    # Load data
    datasets = load_data()

    # Sidebar options
    options = ["Home"] + list(datasets.keys()) + ["Search"]
    choice = st.sidebar.radio("Go to", options)

    # Display selected section
    if choice == "Home":
        st.write("Welcome to the Plant Guide! Use the navigation to explore plants by season or search for specific plants.")
    elif choice in datasets.keys():
        display_category(datasets[choice], choice)
    elif choice == "Search":
        query = st.text_input("Enter plant name to search:")
        if query:
            search_plants(datasets, query)

# Run the app
if __name__ == "__main__":
    main()
