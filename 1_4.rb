def replace_spaces(str, replacing_str)
  spaces_counter = 0
  str.split("").each do |c|
    if c.eql? " " then spaces_counter += 1 end
  end
  str_with_spaces = str << " "*(spaces_counter - 1)*replacing_str.length
  do_replace(str_with_spaces, str_with_spaces.length, replacing_str)
end

def do_replace(str, true_length, replace_with)
	i = 0
	while i < true_length do
		curChar = str[i]
		if curChar == " "
			str = str[0..i-1] + replace_with + str[i+1..str.length]
			# puts str
		end
		i += 1
	end
	str
end

puts replace_spaces("Mr John Smith ", "%20")
