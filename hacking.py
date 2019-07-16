from uagame import Window
from time import sleep
# create window
window = Window('Hacking', 600, 500)
window.set_font_color('blue')
window.set_font_name('couriernew')
window.set_bg_color('black')
window.set_font_size(18)

line_y = 0
string_height = window.get_font_height()

# displaying attemps lef
window.draw_string('1 ATTEMP(S) LEFT' , 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

# displaying password list
window.draw_string('DOG', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('PEPE', 0, line_y)
window.update()
sleep(0.3)  
line_y = line_y + string_height

# prompt user for password
guess = window.input_string('ENTER PASSWORD > ', 0, line_y)

#clear window
window.clear()

# create outcome
if guess == 'PEPE' :
    window.draw_string('SUCCESS!!', 0, 0)
    window.update()
else:
    window.draw_string('FAILURE!!', 0, 0)
    window.update()
    
sleep(2)

# clear window
window.clear()

# prompt for end
window.input_string('PRESS ENTER TO QUITT', 0, line_y)

# close window
window.close()