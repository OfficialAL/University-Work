import random
import time
import os
import sys

def slow_print(text, delay=0.05):
    """Simulates typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Ensures that each character is printed immediately
        time.sleep(delay)
    print()  # For a newline after the text is printed

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Windows uses 'cls', others use 'clear'

# Hostile Entity Class
class Hostile:
    def __init__(self, name, health, attack, defense, speed, loot_table=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.loot_table = loot_table  # Each enemy will have a loot table (can be None)

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage!")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def attack_player(self, player):
        damage = max(0, self.attack - player.defense)
        player.take_damage(damage)
        print(f"{self.name} attacks {player.name} for {damage} damage!")


# Item Class (for Equipment System)
class Item:
    def __init__(self, name, item_type, attack_boost=0, defense_boost=0, description="", cursed=False):
        self.name = name
        self.item_type = item_type  # 'weapon', 'armor', etc.
        self.attack_boost = attack_boost
        self.defense_boost = defense_boost
        self.description = description
        self.cursed = cursed  # If the item is cursed, it may have negative effects


# Sanity Class
class Sanity:
    def __init__(self, max_sanity=100):
        self.max_sanity = max_sanity
        self.current_sanity = max_sanity

    def decrease(self, amount):
        self.current_sanity -= amount
        if self.current_sanity < 0:
            self.current_sanity = 0
        print(f"Sanity decreased by {amount}. Current sanity: {self.current_sanity}")

    def increase(self, amount):
        self.current_sanity += amount
        if self.current_sanity > self.max_sanity:
            self.current_sanity = self.max_sanity
        print(f"Sanity increased by {amount}. Current sanity: {self.current_sanity}")

    def is_insane(self):
        return self.current_sanity <= 0


# Player Class with Equipment System
class Player:
    def __init__(self, name="Nameless Adventurer"):
        self.name = name
        self.health = 100
        self.inventory = []
        self.attack_power = 10
        self.defense = 5
        self.speed = 5
        self.equipped_items = {"weapon": None, "armor": None}  # Tracks equipped items
        self.sanity = Sanity()

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage!")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} found a {item.name}!")
        if item.cursed:
            self.sanity.decrease(10)

    def show_inventory(self):
        print(f"{self.name}'s Inventory:")
        for item in self.inventory:
            print(f"- {item.name} ({item.item_type}): {item.description}")

    def equip_item(self, item):
        if item.item_type == "weapon":
            if self.equipped_items["weapon"]:
                self.unequip_item("weapon")
            self.equipped_items["weapon"] = item
            self.attack_power += item.attack_boost
            print(f"{self.name} equipped {item.name} as a weapon!")
        elif item.item_type == "armor":
            if self.equipped_items["armor"]:
                self.unequip_item("armor")
            self.equipped_items["armor"] = item
            self.defense += item.defense_boost
            print(f"{self.name} equipped {item.name} as armor!")

    def unequip_item(self, item_type):
        if self.equipped_items[item_type]:
            item = self.equipped_items[item_type]
            if item_type == "weapon":
                self.attack_power -= item.attack_boost
            elif item_type == "armor":
                self.defense -= item.defense_boost
            self.equipped_items[item_type] = None
            print(f"{self.name} unequipped the {item.name}!")

    def show_stats(self):
        print(f"{self.name}'s Stats:")
        print(f"Health: {self.health}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")
        print(f"Sanity: {self.sanity.current_sanity}/{self.sanity.max_sanity}")


# Loot Class (Loot Table System)
class Loot:
    def __init__(self, items):
        self.items = items  # List of item objects

    def generate_loot(self):
        """Randomly choose an item from the loot table."""
        loot = random.choice(self.items)
        print(f"Loot found: {loot.name}!")
        return loot


# Define some items
rusty_dagger = Item("Rusty Dagger", "weapon", attack_boost=2, description="A crude but sharp dagger.")
leather_armor = Item("Leather Armor", "armor", defense_boost=3, description="Old, worn leather armor.")
cursed_ring = Item("Cursed Ring", "accessory", attack_boost=5, defense_boost=-3, description="A ring with dark magic.", cursed=True)
potion_of_healing = Item("Potion of Healing", "potion", description="Restores 25 health.")
spider_venom = Item("Spider Venom", "potion", description="Deals 10 damage over time when consumed.")
golem_helmet = Item("Golem Helmet", "armor", defense_boost=5, description="A heavy iron helmet from an ancient golem.")
wolf_pelt = Item("Wolf Pelt", "armor", defense_boost=2, description="A thick, fur pelt that grants warmth and protection.")

# Loot tables for enemies
merman_loot_table = Loot([rusty_dagger, leather_armor, potion_of_healing])
spider_loot_table = Loot([spider_venom, potion_of_healing])  # Spider drops venom or healing
golem_loot_table = Loot([golem_helmet, rusty_dagger])  # Golem drops a helmet or weapon
wolf_loot_table = Loot([wolf_pelt, potion_of_healing])  # Wolf drops a pelt or healing potion


class Game:
    def __init__(self):
        self.player = Player()
        self.locations = {
            "intro": self.intro,
            "ancient_hallway": self.ancient_hallway,
            "lake_entrance": self.lake_entrance,
            "lake_bank": self.lake_bank,
            "lake_bottom": self.lake_bottom,
            "ruinous_city": self.ruinous_city,
        }
        self.current_location = self.locations["intro"]

    def navigate_to(self, location_name):
        if location_name in self.locations:
            self.current_location = self.locations[location_name]
            self.current_location()
        else:
            print("Invalid location!")

    def intro(self):
        slow_print("You are a nameless adventurer...")
        slow_print("You wake in a dark, desolate land. The ruins of forgotten civilizations stretch as far as the eye can see.")
        input("Press Enter to continue...")  # Wait for player input before continuing
        clear_screen()  # Clear the screen after typing the intro text
        self.show_controls()  # Show controls to the player
        self.navigate_to("ancient_hallway")  # Move to next location

    def show_controls(self):
        slow_print("Controls:")
        slow_print("1. Type 'stats' to view your current stats.")
        slow_print("2. Type 'inventory' to view your inventory.")
        slow_print("3. Type 'equip [item name]' to equip an item from your inventory.")
        slow_print("4. Type 'unequip [item type]' to unequip an item (weapon or armor).")
        slow_print("5. Type 'move [direction]' to move in a direction (onwards/backwards).")
        slow_print("6. Type 'attack' to attack an enemy during an encounter.")
        slow_print("7. Type 'run' to attempt to escape an encounter.")
        input("Press Enter to continue...")  # Wait for player input before continuing

    def display_gui(self):
        clear_screen()
        print("====================================")
        print(f"Player: {self.player.name}")
        print(f"Health: {self.player.health}")
        print(f"Attack Power: {self.player.attack_power}")
        print(f"Defense: {self.player.defense}")
        print(f"Speed: {self.player.speed}")
        print(f"Sanity: {self.player.sanity.current_sanity}/{self.player.sanity.max_sanity}")
        print("Inventory:")
        for item in self.player.inventory:
            print(f"- {item.name} ({item.item_type}): {item.description}")
        print("====================================")

    def ancient_hallway(self):
        self.display_gui()
        slow_print("You're standing in a dark hallway...")
        choice = input("Do you move forward or backwards? (onwards/backwards): ").lower()
        if choice == "onwards":
            self.navigate_to("lake_entrance")
        elif choice == "backwards":
            self.navigate_to("ruinous_city")
        else:
            slow_print("Not an option.")
            self.ancient_hallway()

    def lake_entrance(self):
        self.display_gui()
        slow_print("You find yourself at a serene lake...")
        choice = input("Do you swim into the lake or walk along the bank? (walk/dive): ").lower()
        if choice == "walk":
            self.navigate_to("lake_bank")
        elif choice == "dive":
            self.navigate_to("lake_bottom")
        else:
            slow_print("Not an option.")
            self.lake_entrance()

    def lake_bank(self):
        self.display_gui()
        slow_print("You are walking along the lake bank.")
        merman = self.create_enemy("Merman")
        encounter = Encounter(self.player, merman, self)
        encounter.start()

    def lake_bottom(self):
        self.display_gui()
        slow_print("You dive into the mysterious lake...")
        spider = self.create_enemy("Spider")
        encounter = Encounter(self.player, spider, self)
        encounter.start()

    def ruinous_city(self):
        self.display_gui()
        slow_print("You enter a ruinous city filled with danger.")
        golem = self.create_enemy("Golem")
        encounter = Encounter(self.player, golem, self)
        encounter.start()

    def create_enemy(self, name):
        """Factory method to create enemies dynamically."""
        if name == "Merman":
            return Hostile("Merman", health=30, attack=10, defense=5, speed=6, loot_table=merman_loot_table)
        elif name == "Spider":
            return Hostile("Spider", health=20, attack=2, defense=2, speed=6, loot_table=spider_loot_table)
        elif name == "Golem":
            return Hostile("Golem", health=50, attack=15, defense=8, speed=2, loot_table=golem_loot_table)
        elif name == "Wolf":
            return Hostile("Wolf", health=20, attack=5, defense=2, speed=8, loot_table=wolf_loot_table)
        else:
            raise ValueError(f"Unknown enemy: {name}")

    def run(self):
        self.current_location()

    def game_over(self):
        slow_print("\nGAME OVER")
        choice = input("Do you want to restart? (yes/no): ").lower()
        if choice == "yes":
            self.__init__()
            self.run()
        else:
            slow_print("Thanks for playing!")
            exit()


# Encounter Class
class Encounter:
    def __init__(self, player, enemy, game):
        self.player = player
        self.enemy = enemy
        self.game = game

    def start(self):
        slow_print(f"\nYou encounter a {self.enemy.name}!")
        while self.enemy.is_alive() and self.player.health > 0:
            if self.player.sanity.is_insane():
                slow_print("You are too insane to fight properly!")
                self.player.take_damage(5)  # Take damage due to insanity
            action = input("What do you do? (attack/run): ").lower()
            if action == "attack":
                damage = max(0, self.player.attack_power - self.enemy.defense)
                self.enemy.take_damage(damage)
                slow_print(f"You attack the {self.enemy.name} for {damage} damage!")
                if not self.enemy.is_alive():
                    slow_print(f"You defeated the {self.enemy.name}!")
                    # If the enemy is defeated, drop loot
                    if self.enemy.loot_table:
                        loot = self.enemy.loot_table.generate_loot()
                        self.player.add_item(loot)
                    break

            elif action == "run":
                speed_diff = self.player.speed - self.enemy.speed
                if random.randint(1, 10) <= 5 + speed_diff:
                    slow_print("You successfully escape!")
                    return
                else:
                    slow_print("You failed to escape!")

            else:
                slow_print("Invalid action.")

            if self.enemy.is_alive():
                self.enemy.attack_player(self.player)

        if self.player.health <= 0:
            slow_print("\nYou were defeated...")
            self.game.game_over()

# Initialize the game
game = Game()
game.run()
