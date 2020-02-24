# Regular expression

![image regular expression on ruby](https://www.rubyguides.com/wp-content/uploads/2015/06/ruby-regex.png)
A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings using a specialized syntax held in a pattern.

A regular expression literal is a pattern between slashes or between arbitrary delimiters followed by %r as follows −

## Example:

```
#!/usr/bin/ruby

line1 = "Cats are smarter than dogs";
line2 = "Dogs also like meat";

if ( line1 =~ /Cats(.*)/ )
   puts "Line1 contains Cats"
end
if ( line2 =~ /Cats(.*)/ )
   puts "Line2 contains  Dogs"
end
```

# Search and Replace
Some of the most important String methods that use regular expressions are sub and gsub, and their in-place variants sub! and gsub!.

All of these methods perform a search-and-replace operation using a Regexp pattern. The sub & sub! replaces the first occurrence of the pattern and gsub & gsub! replaces all occurrences.

The sub and gsub returns a new string, leaving the original unmodified where as sub! and gsub! modify the string on which they are called.

## Example:

```
#!/usr/bin/ruby

phone = "2004-959-559 #This is Phone Number"

# Delete Ruby-style comments
phone = phone.sub!(/#.*$/, "")   
puts "Phone Num : #{phone}"

# Remove anything other than digits
phone = phone.gsub!(/\D/, "")    
puts "Phone Num : #{phone}"
```
### This will produce the following result:
```
Phone Num : 2004-959-559
Phone Num : 2004959559
```

# List of Regular Expression:

```

.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
```