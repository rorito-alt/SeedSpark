"""
Quick demonstration of the SeedSpark API.
Run: python examples/demo.py
"""

from datetime import date, timedelta
from seedspark.models import Seed, Location, Sprout
from seedspark.storage import SeedStore


def main():
    store = SeedStore(data_dir="data_demo")

    # Create a Seed
    seed = Seed.create(
        title="School Zero-Waste Week",
        goal="Divert 500 kg of waste from landfill through student-led sorting and composting",
        unit="kg",
        target=500,
        start_date=date.today(),
        end_date=date.today() + timedelta(days=14),
        location=Location(type="school", name="Green Valley High School"),
        description="Students measure and sort waste every day. Compost organics, recycle what can be recycled.",
        organizer_name="Eco Club",
        tags=["waste", "schools", "education"],
    )
    store.save(seed)
    print("Created Seed:", seed.id)
    print(seed.to_json())

    # Add some Sprouts
    for name, amount in [("Ananya", 45), ("Rohan", 62), ("Priya", 38), ("Anonymous", 27)]:
        anonymous = name == "Anonymous"
        sprout = Sprout.create(
            contributor_name=name if not anonymous else "Student",
            amount=amount,
            note="Daily collection",
            anonymous=anonymous,
        )
        seed.add_sprout(sprout)

    store.save(seed)
    print("\nAfter contributions:")
    print(f"Progress: {seed.current}/{seed.target} {seed.unit} ({seed.progress_percent():.1f}%)")
    print(f"Status: {seed.status}")


if __name__ == "__main__":
    main()
