import math

# Assignment 1: Design Your Own Class!

class Smartphone:
    """
    Represents a smartphone with attributes like brand, model, storage, and battery.
    Includes methods for common smartphone actions.
    """
    def __init__(self, brand, model, storage, battery_capacity, color="Black"):
        """
        Constructor to initialize a Smartphone object.

        Args:
            brand (str): The brand of the smartphone.
            model (str): The model of the smartphone.
            storage (int): The storage capacity in GB.
            battery_capacity (int): The battery capacity in mAh.
            color (str, optional): The color of the smartphone. Defaults to "Black".
        """
        # Input validation: Check for valid data types and values
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Brand must be a non-empty string.")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Model must be a non-empty string.")
        if not isinstance(storage, int) or storage <= 0:
            raise ValueError("Storage must be a positive integer.")
        if not isinstance(battery_capacity, int) or battery_capacity <= 0:
            raise ValueError("Battery capacity must be a positive integer.")
        if not isinstance(color, str) or not color.strip():
            raise ValueError("Color must be a non-empty string.")

        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_capacity = battery_capacity
        self.color = color.lower()  # Store color in lowercase

        # Initialize private attributes with default values
        self._is_on = False
        self._battery_level = 100
        self._network_connected = False

    def turn_on(self):
        """Turns the smartphone on."""
        if not self._is_on:
            self._is_on = True
            print(f"{self.brand} {self.model} is turning on...")
        else:
            print(f"{self.brand} {self.model} is already on.")

    def turn_off(self):
        """Turns the smartphone off."""
        if self._is_on:
            self._is_on = False
            print(f"{self.brand} {self.model} is turning off...")
        else:
            print(f"{self.brand} {self.model} is already off.")

    def call(self, number):
        """
        Makes a call to the specified number.

        Args:
            number (str): The phone number to call.
        """
        if not isinstance(number, str) or not number.strip():
            raise ValueError("Phone number must be a non-empty string.")
        if self._is_on and self._network_connected:
            print(f"Calling {number} from {self.brand} {self.model}...")
            self._battery_level -= 5  # Simulate battery drain
            self._check_battery()
        elif not self._is_on:
            print(f"Cannot call. {self.brand} {self.model} is off.")
        else:
            print(f"Cannot call. {self.brand} {self.model} is not connected to a network.")

    def send_message(self, message, recipient):
        """
        Sends a text message.

        Args:
            message (str): The message to send.
            recipient (str): The recipient of the message.
        """
        if not isinstance(message, str) or not message.strip():
            raise ValueError("Message must be a non-empty string.")
        if not isinstance(recipient, str) or not recipient.strip():
            raise ValueError("Recipient must be a non-empty string.")
        if self._is_on:
            print(f"Sending message: '{message}' to {recipient} from {self.brand} {self.model}...")
            self._battery_level -= 2  # Simulate battery drain
            self._check_battery()
        else:
            print(f"Cannot send message. {self.brand} {self.model} is off.")

    def connect_to_network(self, network_name=""):
        """Connects the smartphone to a network."""
        if not self._is_on:
            print(f"Cannot connect to network. {self.brand} {self.model} is off.")
            return

        if not network_name:
            print(f"Connecting {self.brand} {self.model} to an available network...")
        else:
            if not isinstance(network_name, str) or not network_name.strip():
                raise ValueError("Network name must be a non-empty string.")
            print(f"Connecting {self.brand} {self.model} to network '{network_name}'...")
        self._network_connected = True
        print(f"{self.brand} {self.model} is now connected to the network.")

    def disconnect_from_network(self):
        """Disconnects the smartphone from the network."""
        if self._is_on and self._network_connected:
            print(f"Disconnecting {self.brand} {self.model} from the network...")
            self._network_connected = False
            print(f"{self.brand} {self.model} is now disconnected from the network.")
        elif not self._is_on:
            print(f"Cannot disconnect. {self.brand} {self.model} is off.")
        else:
            print(f"{self.brand} {self.model} is not connected to any network.")

    def charge(self, duration_minutes):
        """
        Charges the smartphone's battery.

        Args:
            duration_minutes (int): The duration of charging in minutes.
        """
        if not isinstance(duration_minutes, int) or duration_minutes <= 0:
            raise ValueError("Charging duration must be a positive integer.")
        if self._is_on:
            print(f"Charging {self.brand} {self.model} for {duration_minutes} minutes...")
            self._battery_level = min(100, self._battery_level + (duration_minutes / 10))  # Simulate charging
            print(f"Battery level is now {self._battery_level}%.")
        else:
            print(f"Cannot charge {self.brand} {self.model} while it is off. Please turn it on to charge.")

    def get_battery_level(self):
        """Returns the current battery level."""
        return self._battery_level

    def display_info(self):
        """Displays information about the smartphone."""
        print("--- Smartphone Information ---")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Storage: {self.storage} GB")
        print(f"Battery Capacity: {self.battery_capacity} mAh")
        print(f"Battery Level: {self._battery_level}%")
        print(f"Is On: {self._is_on}")
        print(f"Network Connected: {self._network_connected}")
        print("----------------------------")

    def _check_battery(self):
        """
        Checks the battery level and displays a warning if it's low.
        This is a private method (starts with an underscore).
        """
        if self._battery_level < 20:
            print(f"Warning: {self.brand} {self.model} battery is low ({self._battery_level}%). Please charge.")
        elif self._battery_level < 5:
            self.turn_off()

class GamingSmartphone(Smartphone):
    """
    Represents a gaming-focused smartphone, inheriting from the Smartphone class.
    Adds specific attributes and methods for gaming.
    """
    def __init__(self, brand, model, storage, battery_capacity, cooling_system, refresh_rate, color="Black"):
        """
        Constructor for GamingSmartphone.

        Args:
            brand (str): The brand of the gaming smartphone.
            model (str): The model of the gaming smartphone.
            storage (int): The storage capacity.
            battery_capacity (int): The battery capacity.
            cooling_system (str): The type of cooling system.
            refresh_rate (int): The screen refresh rate in Hz.
            color (str, optional): The color of the smartphone. Defaults to "Black".
        """
        super().__init__(brand, model, storage, battery_capacity, color)  # Call parent class constructor
        # Input Validation
        if not isinstance(cooling_system, str) or not cooling_system.strip():
            raise ValueError("Cooling system must be a non-empty string.")
        if not isinstance(refresh_rate, int) or refresh_rate <= 0:
            raise ValueError("Refresh rate must be a positive integer.")
        self.cooling_system = cooling_system
        self.refresh_rate = refresh_rate
        self._game_mode = False  # Added for demonstration

    def enable_game_mode(self):
        """Enables game mode, optimizing performance."""
        if self._is_on:
            self._game_mode = True
            print(f"Game mode enabled on {self.brand} {self.model}. Performance optimized!")
            # Example of using the attributes.
            print(f"Cooling system: {self.cooling_system}, Refresh rate: {self.refresh_rate} Hz")
        else:
            print(f"Cannot enable game mode. {self.brand} {self.model} is off.")

    def disable_game_mode(self):
        """Disables game mode."""
        if self._is_on:
            self._game_mode = False
            print(f"Game mode disabled on {self.brand} {self.model}.")
        else:
            print(f"Cannot disable game mode. {self.brand} {self.model} is off.")

    def play_game(self, game_name):
        """
        Simulates playing a game.

        Args:
            game_name (str): The name of the game.
        """
        if not isinstance(game_name, str) or not game_name.strip():
            raise ValueError("Game name must be a non-empty string.")
        if self._is_on and self._game_mode:
            print(f"Playing {game_name} on {self.brand} {self.model} in game mode!")
            self._battery_level -= 10  # Simulate higher battery drain in game mode
            self._check_battery()
        elif not self._is_on:
            print(f"Cannot play game. {self.brand} {self.model} is off.")
        elif not self._game_mode:
            print(f"Cannot play game. Enable game mode first on {self.brand} {self.model}.")

    def display_info(self):
        """Overrides the parent class's display_info() method to include gaming-specific information."""
        super().display_info()  # Call the parent class's method
        print("--- Gaming Smartphone Information ---")
        print(f"Cooling System: {self.cooling_system}")
        print(f"Refresh Rate: {self.refresh_rate} Hz")
        print(f"Game Mode: {self._game_mode}")
        print("------------------------------------")

# Activity 2: Polymorphism Challenge!

class Animal:
    """Base class representing an animal."""
    def __init__(self, name):
        """Constructor for the Animal class."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        self.name = name

    def move(self):
        """Default move method for animals."""
        print(f"{self.name} moves.")

    def speak(self):
        """Default speak method for animals."""
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    """Represents a dog, inheriting from the Animal class."""
    def __init__(self, name, breed="Unknown"):
        """Constructor for the Dog class."""
        super().__init__(name)
        if not isinstance(breed, str) or not breed.strip():
            raise ValueError("Breed must be a non-empty string.")
        self.breed = breed

    def move(self):
        """Overrides the move method for dogs."""
        print(f"{self.name} the {self.breed} runs.")

    def speak(self):
        """Overrides the speak method for dogs."""
        print(f"{self.name} barks: Woof! Woof!")

class Cat(Animal):
    """Represents a cat, inheriting from the Animal class."""
    def __init__(self, name, color="Unknown"):
        """Constructor for the Cat class."""
        super().__init__(name)
        if not isinstance(color, str) or not color.strip():
            raise ValueError("Color must be a non-empty string.")
        self.color = color

    def move(self):
        """Overrides the move method for cats."""
        print(f"{self.name} the {self.color} cat walks gracefully.")

    def speak(self):
        """Overrides the speak method for cats."""
        print(f"{self.name} meows: Meow!")

class Fish(Animal):
    """Represents a fish, inheriting from the Animal class."""
    def __init__(self, name, type="Unknown"):
        super().__init__(name)
        if not isinstance(type, str) or not type.strip():
            raise ValueError("Type must be a non-empty string.")
        self.type = type
    def move(self):
        print(f"{self.name} the {self.type} swims.")

    def speak(self):
        print(f"{self.name} bubbles.")
class Vehicle:
    """Base class representing a vehicle."""
    def __init__(self, make, model):
        """Constructor for the Vehicle class."""
        if not isinstance(make, str) or not make.strip():
            raise ValueError("Make must be a non-empty string.")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Model must be a non-empty string.")
        self.make = make
        self.model = model

    def move(self):
        """Default move method for vehicles."""
        print(f"The {self.make} {self.model} moves.")

    def display_info(self):
        """Displays Vehicle info"""
        print(f"Make: {self.make}, Model: {self.model}")
class Car(Vehicle):
    """Represents a car, inheriting from the Vehicle class."""
    def __init__(self, make, model, num_doors=4):
        """Constructor for the Car class."""
        super().__init__(make, model)
        if not isinstance(num_doors, int) or num_doors <= 0:
            raise ValueError("Number of doors must be a positive integer.")
        self.num_doors = num_doors

    def move(self):
        """Overrides the move method for cars."""
        print(f"The {self.make} {self.model} drives on the road.")

class Plane(Vehicle):
    """Represents a plane, inheriting from the Vehicle class."""
    def __init__(self, make, model, wingspan):
        """Constructor for the Plane class."""
        super().__init__(make, model)
        if not isinstance(wingspan, (int, float)) or wingspan <= 0:
            raise ValueError("Wingspan must be a positive number.")
        self.wingspan = wingspan

    def move(self):
        """Overrides the move method for planes."""
        print(f"The {self.make} {self.model} flies in the sky.")

    def display_info(self):
        super().display_info()
        print(f"Wingspan: {self.wingspan}")

def main():
    """Main function to demonstrate the classes and polymorphism."""
    # Assignment 1: Smartphone Class
    print("--- Assignment 1: Smartphone Class ---")
    try:
        my_phone = Smartphone("Samsung", "Galaxy S21", 128, 4000, "Violet")
        my_phone.turn_on()
        my_phone.connect_to_network("MyWiFi")
        my_phone.call("123-456-7890")
        my_phone.send_message("Hello!", "John")
        my_phone.display_info()
        my_phone.charge(60)
        my_phone.disconnect_from_network()
        my_phone.turn_off()

        #Demonstrate the GamingSmartphone
        gaming_phone = GamingSmartphone("ROG", "Phone 7", 512, 6000, "Vapor Chamber", 165, "Red")
        gaming_phone.turn_on()
        gaming_phone.enable_game_mode()
        gaming_phone.play_game("Genshin Impact")
        gaming_phone.display_info()
        gaming_phone.charge(90)
        gaming_phone.turn_off()

    except ValueError as e:
        print(f"Error creating/using Smartphone: {e}")

    # Activity 2: Polymorphism Challenge
    print("\n--- Activity 2: Polymorphism Challenge ---")
    animals = [
        Dog("Buddy", "Golden Retriever"),
        Cat("Whiskers", "Gray"),
        Fish("Nemo", "Clownfish")
    ]
    for animal in animals:
        animal.move()
        animal.speak()

    print("\n--- Vehicles ---")
    vehicles = [
        Car("Toyota", "Camry", 4),
        Plane("Boeing", "747", 68.4),
        Car("Ford", "Mustang", 2)
    ]
    for vehicle in vehicles:
        vehicle.move()
        vehicle.display_info()

if __name__ == "__main__":
    main()
