import pandas as pd

# Load dataset
df = pd.read_csv("smarttrip_destinations_dataset.csv")

print("=" * 50)
print("      SmartTrip Recommendation System")
print("=" * 50)

# User Inputs
budget = int(input("\nEnter your budget (INR): "))
interest = input("Enter destination type (Beach, Mountain, Nature, Adventure, Heritage, Religious, Wildlife, Luxury, City, Cultural): ")
duration = int(input("Enter trip duration (days): "))

# Filter destinations
recommended = df[
    (df["avg_trip_cost_inr"] <= budget) &
    (df["destination_type"].str.lower() == interest.lower()) &
    (df["recommended_duration_days"] <= duration)
]

# Sort by rating and popularity
recommended = recommended.sort_values(
    by=["rating", "popularity_score"],
    ascending=False
)

print("\n" + "=" * 50)
print("Top Recommended Destinations")
print("=" * 50)

if recommended.empty:
    print("No destinations found matching your preferences.")
else:
    top_destinations = recommended.head(5)

for i, (_, row) in enumerate(top_destinations.iterrows(), start=1):
    destination = row["destination_name"]
    country = row["country"]
    dtype = row["destination_type"]
    budget = row["avg_trip_cost_inr"]
    duration = row["recommended_duration_days"]
    rating = row["rating"]

    print(f"\n{i}. {destination}")
    print(f"   Country : {country}")
    print(f"   Type    : {dtype}")
    print(f"   Budget  : ₹{budget}")
    print(f"   Duration: {duration} days")
    print(f"   Rating  : {rating}")