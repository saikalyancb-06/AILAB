class DynamicVacuumAgent:
    def __init__(self):
        self.environment = {}
        self.room_order = []  # To maintain the sequence of rooms
        self.vacuum_location = ""
        self.cost = 0

    def setup_user_environment(self):
        print("--- 🛠️ Vacuum Environment Setup ---")
        
        # 1. Input number of rooms
        while True:
            try:
                num_rooms = int(input("Enter the total number of rooms: "))
                if num_rooms > 0:
                    break
                print("Please enter a number greater than 0.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        # 2. Input room names and their status
        for i in range(num_rooms):
            name = input(f"Enter name for Room {i+1}: ").strip().upper()
            while not name:
                name = input(f"Room name cannot be empty. Enter name for Room {i+1}: ").strip().upper()
            
            # Input clean/dirty status
            while True:
                status = input(f"Is {name} Clean (0) or Dirty (1)? Enter 0 or 1: ").strip()
                if status in ['0', '1']:
                    self.environment[name] = int(status)
                    self.room_order.append(name)
                    break
                print("Invalid status. You must enter 0 (Clean) or 1 (Dirty).")

        # 3. Input starting location of the vacuum
        print(f"\nAvailable rooms: {', '.join(self.room_order)}")
        while True:
            start_loc = input("Where is the vacuum cleaner starting? Enter room name: ").strip().upper()
            if start_loc in self.environment:
                self.vacuum_location = start_loc
                break
            print(f"Invalid room. Choose from: {', '.join(self.room_order)}")

    def sense_and_act(self):
        print(f"\n--- 🏁 Initial Environment State ---")
        print(f"Vacuum Location: {self.vacuum_location}")
        for room, status in self.environment.items():
            print(f"Room {room}: {'Dirty' if status == 1 else 'Clean'}")
        print("-----------------------------------")

        current_idx = self.room_order.index(self.vacuum_location)
        direction = 1 

        while any(status == 1 for status in self.environment.values()):
            current_room = self.room_order[current_idx]
            room_status = self.environment[current_room]

            if room_status == 1:  # Condition: Room is Dirty
                print(f"[ACT] Vacuum is in Room {current_room}. Status: DIRTY. Action: SUCK.")
                self.environment[current_room] = 0  # Clean it
                self.cost += 1
                print(f"     -> Room {current_room} is now CLEAN.")
            
            else:  # Condition: Room is Clean, must move
                # Determine next room index based on boundary reflections
                if current_idx == len(self.room_order) - 1 and direction == 1:
                    direction = -1  # Turn around at the right wall
                elif current_idx == 0 and direction == -1:
                    direction = 1   # Turn around at the left wall
                
                next_idx = current_idx + direction
                next_room = self.room_order[next_idx]
                
                action_dir = "RIGHT/FORWARD" if direction == 1 else "LEFT/BACKWARD"
                print(f"[ACT] Vacuum is in Room {current_room}. Status: CLEAN. Action: Move {action_dir} to Room {next_room}.")
                
                current_idx = next_idx
                self.vacuum_location = next_room
                self.cost += 1

        print(f"\n🎉 GOAL REACHED! All rooms are perfectly clean.")
        print(f"Performance Score (Total Actions/Cost): {self.cost}")


# --- Execution ---
if __name__ == "__main__":
    agent = DynamicVacuumAgent()
    agent.setup_user_environment()
    agent.sense_and_act()
