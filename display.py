import pygame

pygame.init()

screen = pygame.display.set_mode((800,480))
clock = pygame.time.Clock()
running = True
plastic_bottle = pygame.image.load("plastic.jpg")
can = pygame.image.load("can.jpg")
paper = pygame.image.load("paper.jpg")
fail = pygame.image.load("fail.jpg")
font = pygame.font.SysFont("Arial Black",25)
text_plastic = font.render("Plastic",True,(0,0,0))
text_can = font.render("Can",True,(0,0,0))
text_paper = font.render("Paper",True,(0,0,0))
text_fail = font.render("Unidentifiable",True,(0,0,0))


def display(prediction):
    screen.fill("white")
    if(prediction == "plastic"):
        screen.blit(text_plastic,(((800 - text_plastic.get_width())/2),((480 - plastic_bottle.get_height())/2)-50)) 
        screen.blit(plastic_bottle,(((800 - plastic_bottle.get_width())/2),((480 - plastic_bottle.get_height())/2)))
    elif (prediction == "can"):
        screen.blit(text_can,(((800 - text_can.get_width())/2),((480 - can.get_height())/2)-50)) 
        screen.blit(can,(((800 - can.get_width())/2),((480 - can.get_height())/2)))
    elif (prediction == "paper"):
        screen.blit(text_paper,(((800 - text_paper.get_width())/2),((480 - paper.get_height())/2)-50)) 
        screen.blit(paper,(((800 - paper.get_width())/2),((480 - paper.get_height())/2)))
    elif(prediction == "fail"):
        screen.blit(text_fail,(((800 - text_fail.get_width())/2),((480 - fail.get_height())/2)-50)) 
        screen.blit(fail,(((800 - fail.get_width())/2),((480 - fail.get_height())/2)))
    
    
prediction = ''
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        prediction = "plastic"
    if keys[pygame.K_s]:
        prediction = "can"
    if keys[pygame.K_d]:
        prediction = "paper"
    if keys[pygame.K_f]:
        prediction = "fail"
    display(prediction)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()