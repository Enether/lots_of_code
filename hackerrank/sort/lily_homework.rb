require 'pp'
require 'set'

gets
array = gets.chomp.split(' ').map{|x| x.to_i}

# the sorted indices
goal_indices = {}

def swap_number_to_match(array, goal_indices)
  # Imagine the connections between the current indices
  # and the goal indices as a graph and traverse
  # through each cycle of pairs of indices,
  # calculating the number of needed swaps
  visited_indices = Set.new
  overall_moves = 0

  array.each_with_index do |val, key|
    # start going into a cycle, only into indices we have not visited
    visited_indices.add key

    next_node = goal_indices[val]
    moves = 0
    until visited_indices.include? next_node
      visited_indices.add next_node
      # get the value at the index we're at
      next_node_val = array[next_node]
      next_node = goal_indices[next_node_val]
      moves += 1
    end
    overall_moves += moves
  end

  overall_moves
end

# populate goal_indices normally
array.sort.each_with_index { |val, idx| goal_indices[val] = idx }
normal_sort_swap_count = swap_number_to_match(array, goal_indices)

# populate with reversed sorted array
array.sort.reverse.each_with_index { |val, idx| goal_indices[val] = idx}
reversed_sort_swap_count = swap_number_to_match(array, goal_indices)

# get the minimum of both possible sorts (normal and reversed)
puts [reversed_sort_swap_count, normal_sort_swap_count].min
