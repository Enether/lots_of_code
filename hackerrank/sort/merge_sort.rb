$inversion_count = 0

def merge_sort(arr, start_idx, end_idx)
  array_length = end_idx - start_idx
  return arr[start_idx...end_idx].sort if array_length <= 2

  median = ((end_idx - start_idx) / 2) + start_idx
  sorted_array = []

  first_part = merge_sort(arr, start_idx, median+1)
  second_part = merge_sort(arr, median+1, end_idx)

  # merge both arrays
  first_idx = 0
  second_idx = 0

  while first_idx < first_part.length or second_idx < second_part.length
    if first_idx < first_part.length and second_idx < second_part.length
      # have both arrays to work with
      first_el, second_el = first_part[first_idx], second_part[second_idx]
      if first_el > second_el
        $inversion_count += 1
        # puts "#{first_el} is bigger than #{second_el}"
        # take lesser element - second_part
        sorted_array << second_el
        second_idx += 1
      else
        # take first element
        $inversion_count += 1

        sorted_array << first_el
        first_idx += 1
      end
    elsif first_idx < first_part.length
      $inversion_count += 1
      # only first part is left, copy out everything in it
      while first_idx < first_part.length
        sorted_array << first_part[first_idx]
        first_idx += 1
      end
    elsif second_idx < second_part.length
      # $inversion_count += 1
      while second_idx < second_part.length
        sorted_array << second_part[second_idx]
        second_idx += 1
      end
    end
  end

  sorted_array
end


query_count = gets.chomp.to_i
(0...query_count).each do | |
  gets
  array = gets.chomp.split(' ').map(&:to_i)
  $inversion_count = 0
  merge_sort(array, 0, array.length)
  puts($inversion_count)
end
