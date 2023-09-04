import pygame
class Display:
    def __init__(self):
        self.running = True
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,480))
        self.clock = pygame.time.Clock()
        self.running = True
        self.plastic_bottle = pygame.image.load("Images/plastic.jpg")
        self.can = pygame.image.load("Images/can.jpg")
        self.paper = pygame.image.load("Images/paper.jpg")
        self.fail = pygame.image.load("Images/fail.jpg")
        self.font = pygame.font.SysFont("Arial",25)
        self.text_plastic = self.font.render("Plastic",True,(0,0,0))
        self.text_can = self.font.render("Can",True,(0,0,0))
        self.text_paper = self.font.render("Paper",True,(0,0,0))
        self.text_fail = self.font.render("Unidentifiable",True,(0,0,0))

    def display(self,prediction):
        self.screen.fill("white")
        if(prediction == "plastic"):
            self.screen.blit(self.text_plastic,(((800 - self.text_plastic.get_width())/2),((480 - self.plastic_bottle.get_height())/2)-50)) 
            self.screen.blit(self.plastic_bottle,(((800 - self.plastic_bottle.get_width())/2),((480 - self.plastic_bottle.get_height())/2)))
        elif (prediction == "can"):
            self.screen.blit(self.text_can,(((800 - self.text_can.get_width())/2),((480 - self.can.get_height())/2)-50)) 
            self.screen.blit(self.can,(((800 - self.can.get_width())/2),((480 - self.can.get_height())/2)))
        elif (prediction == "paper"):
            self.screen.blit(self.text_paper,(((800 - self.text_paper.get_width())/2),((480 - self.paper.get_height())/2)-50)) 
            self.screen.blit(self.paper,(((800 - self.paper.get_width())/2),((480 - self.paper.get_height())/2)))
        elif(prediction == "fail"):
            self.screen.blit(self.text_fail,(((800 - self.text_fail.get_width())/2),((480 - self.fail.get_height())/2)-50)) 
            self.screen.blit(self.fail,(((800 - self.fail.get_width())/2),((480 - self.fail.get_height())/2)))
        
    def main(self):
        self.init()
        prediction = ''
        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                prediction = "plastic"
            if keys[pygame.K_s]:
                prediction = "can"
            if keys[pygame.K_d]:
                prediction = "paper"
            if keys[pygame.K_f]:
                prediction = "fail"
            self.display(prediction)
            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()