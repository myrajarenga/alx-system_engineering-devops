#!/usr/bin/env ruby
text = "From +1 (123) 456-7890 to +44 (567) 890-1234 using flags: urgent, high priority"

# Regular expression pattern to extract sender and receiver information
pattern = /From\s(\+\d{1,2}\s\(\d{3}\)\s\d{3}-\d{4}|\w+)\sto\s(\+\d{1,2}\s\(\d{3}\)\s\d{3}-\d{4}|\w+)\susing\sflags:\s(.+)/

# Match the pattern with the text
match = pattern.match(text)

# Extract sender, receiver, and flags information from the match
if match
  sender = match[1]
  receiver = match[2]
  flags = match[3]
  
  # Output the extracted information
  puts "#{sender},#{receiver},#{flags}"
else
  puts "No matching information found"
end

