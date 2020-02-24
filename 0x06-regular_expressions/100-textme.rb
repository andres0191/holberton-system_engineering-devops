#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:|flags:|to:)([a-zA-Z0-9.+-:]{0,9}+)/).join(",")
