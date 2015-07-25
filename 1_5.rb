def compress(str)
	curChar = str[0]
	curCount = 1
	i = 1
	result = ""
	while i < str.length
		if str[i] == curChar
			curCount += 1
		else
			result += curChar
			result += curCount.to_s
			curChar = str[i]
			curCount = 1
		end
		i += 1
	end
	result += curChar
	result += curCount.to_s
	result
end

puts compress("aabcccccaaad")