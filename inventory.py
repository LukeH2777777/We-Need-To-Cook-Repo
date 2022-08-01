class Inventory:

    @staticmethod
    def get_guns() -> dict:
        guns_map = {
            "Machete":
                {
                    "Name": "Machete",
                    "Damage": 50,
                    "Accuracy": 0,
                    "Durability": 0
                },
            "Ak-47":
                {
                    "Name": "Ak-47",
                    "Damage": 100,
                    "Accuracy": 0,
                    "Durability": 0
                },
            "Ar-15":
                {
                    "Name": "Ar-15",
                    "Damage": 80,
                    "Accuracy": 0,
                    "Durability": 0
                },
            "Mp5":
                {
                    "Name": "Mp5",
                    "Damage": 80,
                    "Accuracy": 0,
                    "Durability": 0
                },
            "Glock-19":
                {
                    "Name": "Glock-19",
                    "Damage": 100,
                    "Accuracy": 0,
                    "Durability": 0
                },
            "Fn-seven":
                {
                    "Name": "Fn-seven",
                    "Damage": 90,
                    "Accuracy": 0,
                    "Durability": 0
                }
        }
        return guns_map

    @staticmethod
    def get_foods() -> dict:
        foods_map = {
            "Apple":
                {
                    "Name": "Apple",
                    "Heal": 40,
                    "Add": 0
                },
            "Banana":
                {
                    "Name": "Banana",
                    "Heal": 100,
                    "Add": 0
                },
            "Steak":
                {
                    "Name": "Steak",
                    "Heal": 0,
                    "Add": 20
                },
            "Bolognese":
                {
                    "Name": "Bolognese",
                    "Heal": 0,
                    "Add": 100
                },
            "HomersDonut":
                {
                    "Name": "HomersDonut",
                    "Heal": 0,
                    "Add": 1000
                }
        }
        return foods_map

    @staticmethod
    def get_drugs() -> dict:
        drugs_map = {
            "Weed": 1,
            "Acid": 1,
            "Meth": 1,
            "Cocaine": 1,
            "Crack": 1,
        }
        return drugs_map