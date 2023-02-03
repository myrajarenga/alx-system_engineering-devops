#!/usr/bin/env ruby
puts ARGV[0].scan(/From\s(\+\d{1,2}\s\(\d{3}\)\s\d{3}-\d{4}|\w+)\sto\s(\+\d{1,2}\s\(\d{3}\)\s\d{3}-\d{4}|\w+)\susing\sflags:\s(.+)/).join
