while numbers:
    puts "How many numbers would you like to work with?"
    numbers = gets.chomp

    if numbers == '1'
        puts "Great! What will the first number be?"
        num1 = gets.chomp.to_i

    elsif numbers == '2'
        puts "Great! What will the first number be?"
        num1 = gets.chomp.to_i
        puts "What will the second number be?:"
        num2 = gets.chomp.to_i
    else
        print "I can only work with 1 or 2 numbers."
        puts "How many numbers would you like to work with?"
    end