def split_commands(commands)
  commands.chars.each_slice(2).map(&:join).to_a
end

def shift(commands)
  command = commands.shift
  raise StandardError if command != command.upcase
  command
end

def codeObfuscation(data, program)
  number = -1
  text = -2
  parent_classes = {
      1 => number,
      2 => number,
      3 => number,
      4 => number,
      5 => text,
      6 => text
  }
  two_nums = [number, number]
  commands_dict = {
    '01' => two_nums,
    '4A' => two_nums,
    '13' => two_nums,
    'S2' => two_nums,
    '11' => [number],
    '3F' => [number],
    '99' => [text, text],
    'G0' => [text, number]
  }
  data = data.map {|d| parent_classes[d]}
  commands = split_commands(program)
  until commands.empty?
    begin
      current_command = shift(commands)
      return true if current_command == '0R'

      command = commands_dict[current_command]
      return false if command.nil?
      current_data = data[Integer("0x#{shift(commands)}")]
      # run the command
      puts "Running #{command} with #{current_data}"
      command.each_with_index do |part, idx|
        current_data = data[Integer("0x#{shift(commands)}")] if idx != 0
        return false if part != current_data
      end

    rescue StandardError => e
      puts "Raised #{e}"
      return false
    end
  end
  true
end
puts codeObfuscation([2], "0100000R")
