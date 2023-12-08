import pygame
import sys
from core.game import Game

def show_menu():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Sigrun Adventures Menu")

    font = pygame.font.Font(None, 36)
    text = font.render("Choose the number of enemies:", True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 200))

    options = ["1", "2", "3", "4"]
    option_rects = []
    for i, option in enumerate(options):
        option_text = font.render(option, True, (255, 255, 255))
        option_rect = option_text.get_rect(center=(400, 300 + i * 50))
        option_rects.append((option, option_rect))

    selected_option = options[0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = options.index(selected_option)
                    selected_index = (selected_index - 1) % len(options)
                    selected_option = options[selected_index]
                elif event.key == pygame.K_DOWN:
                    selected_index = options.index(selected_option)
                    selected_index = (selected_index + 1) % len(options)
                    selected_option = options[selected_index]
                elif event.key == pygame.K_RETURN:
                    return int(selected_option)
            elif event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1:  
                    return int(selected_option)

        screen.fill((0, 0, 30))
        screen.blit(text, text_rect)

        for option, option_rect in option_rects:
            color = (255, 255, 255) if option == selected_option else (128, 128, 128)
            pygame.draw.rect(screen, color, option_rect)
            screen.blit(font.render(option, True, (0, 0, 0)), option_rect)

        pygame.display.flip()

def main():
    global game
    try: 
        num_enemies = show_menu()

        pygame.init()

        image_files = [
            "core/assets/sigrun/s1.png",
            "core/assets/sigrun/s2.png",
            "core/assets/sigrun/s3.png",
            "core/assets/sigrun/s4.png",
            "core/assets/sigrun/s5.png",
            "core/assets/sigrun/s6.png",
            "core/assets/sigrun/s7.png",
        ]

        goblin_images = [
            "core/assets/enemies/goblin/goblin_1.png",
            "core/assets/enemies/goblin/goblin_2.png",
            "core/assets/enemies/goblin/goblin_3.png",
            "core/assets/enemies/goblin/goblin_4.png",
            "core/assets/enemies/goblin/goblin_5.png",
            "core/assets/enemies/goblin/goblin_6.png",
            "core/assets/enemies/goblin/goblin_7.png",
            "core/assets/enemies/goblin/goblin_8.png",
        ]

        
        hongo_images = [
            "core/assets/enemies/honguito/honguito_1.png",
            "core/assets/enemies/honguito/honguito_2.png",
            "core/assets/enemies/honguito/honguito_3.png",
            "core/assets/enemies/honguito/honguito_4.png",
        ]

        
        enemy_images = [goblin_images, hongo_images]

        image_gun = pygame.image.load("core/assets/weapons/weapon.png")
        image_bullet = pygame.image.load("core/assets/weapons/bullet.png")

        game = Game(image_files, image_gun, image_bullet, enemy_images, num_enemies)
        game.run()

        show_game_over_auto()

    except Exception as e:
        print("Error:", e)
    finally:
        pygame.quit()
        sys.exit()
    
def show_game_over_auto():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Sigrun Adventures Game Over")

    font = pygame.font.Font(None, 36)
    text = font.render("Game Over - All enemies defeated!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 200))

    end_time = pygame.time.get_ticks() + 3000  # 3000 milisegundos (3 segundos)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current_time = pygame.time.get_ticks()
        if current_time >= end_time:
            break

        screen.fill((0, 0, 30))
        screen.blit(text, text_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
