from hyperdb import HypergraphDB

# Initialize the hypergraph
hg = HypergraphDB()

# Add vertices
hg.add_v(1, {"name": "Alice", "age": 30, "city": "New York"})
hg.add_v(2, {"name": "Bob", "age": 24, "city": "Los Angeles"})
hg.add_v(3, {"name": "Charlie", "age": 28, "city": "Chicago"})
hg.add_v(4, {"name": "David", "age": 35, "city": "Miami"})
hg.add_v(5, {"name": "Eve", "age": 22, "city": "Seattle"})
hg.add_v(6, {"name": "Frank", "age": 29, "city": "Houston"})
hg.add_v(7, {"name": "Grace", "age": 31, "city": "Phoenix"})
hg.add_v(8, {"name": "Heidi", "age": 27, "city": "San Francisco"})
hg.add_v(9, {"name": "Ivan", "age": 23, "city": "Denver"})
hg.add_v(10, {"name": "Judy", "age": 26, "city": "Boston"})

# Add hyperedges
hg.add_e((1, 2, 3), {"type": "friendship", "duration": "5 years"})
hg.add_e((1, 4), {"type": "mentorship", "topic": "career advice"})
hg.add_e((2, 5, 6), {"type": "collaboration", "project": "AI Research"})
hg.add_e((4, 5, 7, 9), {"type": "team", "goal": "community service"})
hg.add_e((3, 8), {"type": "partnership", "status": "ongoing"})
hg.add_e((9, 10), {"type": "neighbors", "relationship": "friendly"})
hg.add_e((1, 2, 3, 7), {"type": "collaboration", "field": "music"})
hg.add_e((2, 6, 9), {"type": "classmates", "course": "Data Science"})

print(hg.nbr_v(1))  # Example Output: {2, 7}
hg.add_e((1, 4, 6), {"relation": "team"})
print(hg.nbr_v(1))  # Example Output: {2, 4, 6, 7}

# Get incident hyperedges of a vertex
print(hg.nbr_e_of_v(1))  # Example Output: {(1, 2, 7), (1, 2), (1, 4, 6)}