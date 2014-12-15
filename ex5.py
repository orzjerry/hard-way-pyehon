my_name = 'Zeb A.shaw'
my_age = 35 # not a lie
my_height_inches = 74 # inches
my_weight_lbs = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

cm = 2.54 #cm
kgs = 0.4535 #kgs

my_height_cm = my_height_inches * cm
my_weight_kgs = my_weight_lbs * kgs

print "Let's talk aboyt %s." % my_name
print "He's %d inches tall." % my_height_inches
print "He's %d cm tall." % my_height_cm
print "He;s %d pounds heavy." % my_weight_lbs
print "He;s %d kgs heavy." % my_weight_kgs
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d. " % (
     my_age, my_height_inches, my_weight_lbs, my_age + my_height_inches + my_weight_lbs)
     