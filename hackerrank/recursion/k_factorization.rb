# non over-engineered version

@goal_num, = gets.chomp.split.map {|p| p.to_i}
@nums = gets.chomp.split.map {|p| p.to_i}.sort.reverse

curr_num = @goal_num
chosen_factors = [@goal_num]
solution_exists = false

while curr_num != 1
  # find the biggest number in @nums
  @nums.each do |n|
    if curr_num % n == 0
      curr_num /= n
      chosen_factors.push curr_num
      solution_exists = true
      break
    end
  end

  break unless solution_exists
  solution_exists = false
end
if curr_num != 1
  puts '-1'
else
  puts "#{chosen_factors.reverse.join ' '}"
end
