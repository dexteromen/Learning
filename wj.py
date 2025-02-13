from collections import deque

class WaterJugProblemBFS:
    def __init__(self, CAP_J3, CAP_J4, TARGET):
        self.CAP_J3 = CAP_J3  # 3-gallon jug
        self.CAP_J4 = CAP_J4  # 4-gallon jug
        self.TARGET = TARGET  # Target water amount in J4 (larger jug)

    def bfs(self):
        # Initial state (0, 0): both jugs are empty
        initial_state = (0, 0)
        
        # Queue for BFS, starting with the initial state
        queue = deque([(initial_state, [])])
        
        # Set to keep track of visited states
        visited = set([initial_state])
        
        while queue:
            (j3, j4), path = queue.popleft()
            
            # If we reach the TARGET in the 4-gallon jug (J4), return the solution path
            if j4 == self.TARGET:
                return path, (j3, j4)
            
            # List of possible actions and resulting states
            actions = [
                ("Fill J3", (self.CAP_J3, j4)),
                ("Fill J4", (j3, self.CAP_J4)),
                ("Empty J3", (0, j4)),
                ("Empty J4", (j3, 0)),
                ("Pour from J3 to J4", (max(0, j3 - (self.CAP_J4 - j4)), min(self.CAP_J4, j4 + j3))),
                ("Pour from J4 to J3", (min(self.CAP_J3, j3 + j4), max(0, j4 - (self.CAP_J3 - j3))))
            ]
            
            # Explore all possible actions
            for action, (new_j3, new_j4) in actions:
                new_state = (new_j3, new_j4)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [(action, new_j3, new_j4)]))
        
        # If no solution is found, return an empty list
        return [], (0, 0)

    def display_solution(self, solution_path, final_state):
        if solution_path:
            print("Solution path to reach the TARGET:")
            for action, j3, j4 in solution_path:
                print(f"{action}: J3 = {j3} gallons, J4 = {j4} gallons")
            print(f"Final state: J3 = {final_state[0]} gallons, J4 = {final_state[1]} gallons")
            print(f"You have exactly {self.TARGET} gallons in J4!")
        else:
            print(f"No solution found to reach {self.TARGET} gallons in J4.")

# Example usage
CAP_J3 = 3  # 3-gallon jug
CAP_J4 = 4  # 4-gallon jug
TARGET = 2  # Target is 2 gallons in J4

# Create an instance of the BFS solution
problem = WaterJugProblemBFS(CAP_J3, CAP_J4, TARGET)

# Run BFS to find the solution
solution_path, final_state = problem.bfs()

# Display the solution path and final state
problem.display_solution(solution_path, final_state)
