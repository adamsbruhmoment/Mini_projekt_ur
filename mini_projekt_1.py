#import necessary python libraries
import pygame 
import math
import datetime

pygame.init() #initializes the python library
screen = pygame.display.set_mode((800, 800)) #creates a 800x800 display

font = pygame.font.Font(None, 32) #sets parameters for the font used later

#sets up variables that will be used later
start_point = (400, 400)
second_arm = 210
min_arm = 190
hour_arm = 160
divot_length = 20

while True: #infinite loop that continuously updates the code below
    #checks for events, if the window is closed, the program quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.fill((255, 0, 200)) #sets the background color
    pygame.draw.circle(screen,(255, 255, 255), start_point, 230) #creates a white circle behind the watch

    current_time = datetime.datetime.now() #sets current_time to the current time

    seconds = current_time.second - 16 + current_time.microsecond / 1000000 #sets seconds at the current time in seconds. 
                                                                            #Time in microseconds/1000000 is added to run more smooth
    angle_second = seconds * 6 #angle for the second timer is set to seconds * 6 (360 degrees divided by seconds in a minute)

    #sets the end point for the second hand
    end_second = (start_point[0] + int(math.cos(math.radians(angle_second)) * second_arm),
             start_point[1] + int(math.sin(math.radians(angle_second)) * second_arm))


    min = current_time.minute + seconds / 60 #sets min to current time in minutes. 
                                             #Time in seconds/60 is added to run more smooth
    angle_min = min * 6 - 90 #angle for minute is set. 90 degrees are substracted for adjustment
    #sets the end point for minute hand
    end_min = (start_point[0] + int(math.cos(math.radians(angle_min)) * min_arm),
               start_point[1] + int(math.sin(math.radians(angle_min)) * min_arm))
  
    hour = (current_time.hour % 12) +  (min / 60) #sets hour to current time in hours.
                                                  #Modulus 12 is added, because clocks only have 12 hours, not 24
                                                  #Time in minutes/60 is added to run more smooth
    angle_hour = hour * 30 - 90 #angle for hour is set. 90 degrees are substracted for adjustment
    #sets the end point for hour hand
    end_hour =(start_point[0] + int(math.cos(math.radians(angle_hour)) * hour_arm),
               start_point[1] + int(math.sin(math.radians(angle_hour)) * hour_arm))

    #draws all three clock hands
    pygame.draw.line(screen, (255,0,0), start_point, end_second)
    pygame.draw.line(screen, (0,255,0), start_point, end_min, 3)
    pygame.draw.line(screen, (0,0,255), start_point, end_hour, 5)

    #draws clock circle
    pygame.draw.circle(screen,(0,0,0), start_point, 230, 5)

    for i in range (60): #for loop to create the smaller divots, indicating minutes. 
        small_angle = i * 6 #sets angle/spacing for small divots
        #sets the starting point for small divots
        small_start = (start_point[0] + int(math.cos(math.radians(small_angle))
                                             * (230 - divot_length / 2)),
                        start_point[1] + int(math.sin(math.radians(small_angle))
                                             * (230 - divot_length / 2)))
        #sets the end point for small divots
        small_end = (start_point[0] + int(math.cos(math.radians(small_angle)) * 230),
                     start_point[1] + int(math.sin(math.radians(small_angle)) * 230))
        #draws the smaller divots
        pygame.draw.line(screen, (0,0,0), small_start, small_end)


    for i in range (12): #for loop to create divots indicating hours
        divot_angle = i * 30 #sets angle/spacing for divots
        #sets the starting point for divots
        divot_start = (start_point[0] + int(math.cos(math.radians(divot_angle)) * (230 - divot_length)),
                       start_point[1] - int(math.sin(math.radians(divot_angle)) * (230 - divot_length)))
        #sets the end point for divots
        divot_end = (start_point[0] + int(math.cos(math.radians(divot_angle)) * 230),
                     start_point[1] - int(math.sin(math.radians(divot_angle)) * 230))
        #draws the divots
        pygame.draw.line(screen, (0,0,0), divot_start, divot_end, 3)

        numbers_angle = 60 - divot_angle  # Calculate the angle (in degrees) for each number position
        #calculate the x and y values for the numbers around the clock
        divot_x = start_point[0] + int(math.cos(math.radians(numbers_angle)) * 250)
        divot_y = start_point[1] - int(math.sin(math.radians(numbers_angle)) * 250)
    
        # Add numbers to the watch
        number_text = font.render(str(i + 1), True, (0, 0, 0)) #Creates text of the numbers
        text_rect = number_text.get_rect() #gets a rectangle representing the text
        text_rect.center = (divot_x, divot_y) #sets center of the text to the calculated x and y positions
        screen.blit(number_text, text_rect) #draws the numbers

    pygame.display.flip() #updates the display to make everything visible