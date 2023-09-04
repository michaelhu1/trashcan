import pygame
class Display:
    def __init__(self,prediction):
        self.running = True
        self.prediction = prediction
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
        self.screen.fill((255,255,255))
        if(prediction == "Plastic"):
            self.screen.blit(self.text_plastic,(((800 - self.text_plastic.get_width())/2),((480 - self.plastic_bottle.get_height())/2)-50)) 
            self.screen.blit(self.plastic_bottle,(((800 - self.plastic_bottle.get_width())/2),((480 - self.plastic_bottle.get_height())/2)))
        elif (prediction == "Can"):
            self.screen.blit(self.text_can,(((800 - self.text_can.get_width())/2),((480 - self.can.get_height())/2)-50)) 
            self.screen.blit(self.can,(((800 - self.can.get_width())/2),((480 - self.can.get_height())/2)))
        elif (prediction == "Paper"):
            self.screen.blit(self.text_paper,(((800 - self.text_paper.get_width())/2),((480 - self.paper.get_height())/2)-50)) 
            self.screen.blit(self.paper,(((800 - self.paper.get_width())/2),((480 - self.paper.get_height())/2)))
        elif(prediction == "Fail"):
            self.screen.blit(self.text_fail,(((800 - self.text_fail.get_width())/2),((480 - self.fail.get_height())/2)-50)) 
            self.screen.blit(self.fail,(((800 - self.fail.get_width())/2),((480 - self.fail.get_height())/2)))
        
    def main(self):
        self.init()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.prediction.prediction = "Plastic"
            if keys[pygame.K_s]:
                self.prediction.prediction = "Can"
            if keys[pygame.K_d]:
                self.prediction.prediction = "Paper"
            if keys[pygame.K_f]:
                self.prediction.prediction = "Fail"
            self.display(self.prediction.prediction)
            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()