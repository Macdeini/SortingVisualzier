import pygame
import random
import sys
SCREEN_WIDTH, SCREEN_HEIGHT = 1880, 1000
DELAY = 1


def force_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


def draw_list(screen, lst, curr=None):
    force_quit()
    screen.fill("black")
    starting_pos = 100
    bar_width = 10
    colors = ["white", "yellow", "blue", "red", "green", "purple", "orange", "black"]
    for x_offset, y_offset in enumerate(lst):
        bar = pygame.Rect(starting_pos + bar_width * x_offset, 0, bar_width, bar_width * y_offset)
        if x_offset == curr:
            pygame.draw.rect(screen, colors[3], bar)
        else:
            pygame.draw.rect(screen, colors[0], bar)
        pygame.draw.line(screen, colors[-1], (starting_pos + bar_width * x_offset, 0), (starting_pos + bar_width * x_offset,bar_width * y_offset))
    pygame.display.update()


def visual_bubble_sort(screen, lst):
    size = len(lst)
    for i in range(size):
        for j in range(size-i-1):
            if lst[j] >= lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            draw_list(screen, lst, j+1)
            pygame.time.wait(DELAY)
            pygame.event.pump()


def visual_insertion_sort(screen, lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        draw_list(screen, lst, i)
        pygame.time.wait(DELAY)
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
        draw_list(screen, lst, j+1)
        pygame.time.wait(DELAY)
        pygame.event.pump()


def visual_selection_sort(screen, lst):
    for i in range(len(lst)):
        min_idx = i
        draw_list(screen, lst, i)
        pygame.time.wait(DELAY)
        for j in range(i+1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        draw_list(screen, lst, min_idx)
        pygame.time.wait(DELAY)
        pygame.event.pump()


def get_menu_option():
    pos = (0, 0)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
        elif event.type == pygame.QUIT:
            sys.exit()
    if 100 <= pos[0] <= 100+100 and 925 <= pos[1] <= 925+50:
        return "randomize"
    elif 100+155 <= pos[0] <= 100+155+100 and 925 <= pos[1] <= 925+50:
        return visual_bubble_sort
    elif 100+155*2 <= pos[0] <= 100+155*2+100 and 925 <= pos[1] <= 925+50:
        return visual_selection_sort
    elif 100+155*3 <= pos[0] <= 100+155*3+100 and 925 <= pos[1] <= 925+50:
        return visual_insertion_sort
    else:
        return None


def draw_buttons(screen):
    randomize_button = pygame.Rect(100, 925, 100, 50)
    bubble_button = pygame.Rect(100+155, 925, 100, 50)
    selection_button = pygame.Rect(100+155*2, 925, 100, 50)
    insertion_button = pygame.Rect(100+155*3, 925, 100, 50)
    pygame.draw.rect(screen, "white", randomize_button, 0, 10)
    pygame.draw.rect(screen, "white", bubble_button, 0, 10)
    pygame.draw.rect(screen, "white", selection_button, 0, 10)
    pygame.draw.rect(screen, "white", insertion_button, 0, 10)
    comic_sans = pygame.font.SysFont('Comic Sans MS', 12)
    randomize_text = comic_sans.render("Randomize", False, "black")
    bubble_text = comic_sans.render("Bubble Sort", False, "black")
    selection_text = comic_sans.render("Selection Sort", False, "black")
    insertion_text = comic_sans.render("Insertion Sort", False, "black")
    screen.blit(randomize_text, (100+10, 925+10))
    screen.blit(bubble_text, (100+155+10, 925+10))
    screen.blit(selection_text, (100+155*2+10, 925+10))
    screen.blit(insertion_text, (100+155*3+10, 925+10))
    pygame.display.update()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
    pygame.display.set_caption("Sort Visuals")
    lst = [random.randint(1, 90) for _ in range(150)]
    draw_list(screen, lst)
    draw_buttons(screen)
    running = False
    while not running:
        option = get_menu_option()
        if option == "randomize":
            lst = [random.randint(1, 90) for _ in range(150)]
            draw_list(screen, lst)
        elif option is not None:
            option(screen, lst)
        draw_buttons(screen)
    pygame.quit()


if __name__ == '__main__':
    main()
