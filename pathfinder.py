class Pathfinder(object):
    def __init__(self, ai_node, maze, node_list, goal_node):
        self.ai_node = ai_node
        self.maze_array = maze
        self.node_list == node_list
        self.goal_node = goal_node

    def calculate_path(self):
        open_list = set()
        closed_list = set()
        current = self.ai_node

        while open_list:
            right_node = node_list[current[1] * 15 + current[0] + 1]
            left_node = node_list[current[1] * 15 + current[0] - 1]
            above_node = node_list[current[1] * 15 + current[0] - 15]
            below_node = node_list[current[1] * 15 + current[0] + 15]
            adjacent_list = set()
            if right_node.value != 1 and right_node not in open_list:
                adjacent_list.add(right_node)
            if left_node.value != 1 and left_node not in open_list:
                adjacent_list.add(left_node)
            if above_node.value != 1 and above_node not in open_list:
                adjacent_list.add(above_node)
            if below_node.value != 1 and below_node not in open_list:
                adjacent_list.add(below_node)
            adjacent_list.add(3)             
            current = min(open_list)
            if current == self.goal_node:
                return open_list
            open_list.remove(current)
            closed_list.add(current)

        

    
        
