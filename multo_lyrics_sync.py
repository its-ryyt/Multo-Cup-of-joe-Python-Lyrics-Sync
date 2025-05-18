import time
import threading
import pygame
import math
import os

# Lyrics with timestamps
lyrics = [
    (3.74, "Multo - Cup of Joe"),
    (22.76, "Humingang malalim, pumikit na muna"),
    (31.76, "At baka sakaling namamalikmata lang"),
    (40.85, "Ba't nababahala? 'Di ba't ako'y mag-isa?"),
    (50.27, "Kala ko'y payapa, boses mo'y tumatawag pa"),
    (59.82, "Binaon naman na ang lahat"),
    (64.39, "Tinakpan naman na 'king sugat"),
    (68.84, "Ngunit ba't ba andito pa rin?"),
    (74.06, "Hirap na 'kong intindihin"),
    (78.05, "Tanging panalangin, lubayan na sana"),
    (86.88, "Dahil sa bawat tingin, mukha mo'y nakikita"),
    (96.43, "Kahit sa'n man mapunta ay anino mo'y kumakapit sa 'king kamay"),
    (105.63, "Ako ay dahan-dahang nililibing ng buhay pa"),
    (114.84, "Hindi na makalaya"),
    (119.40, "Dinadalaw mo 'ko bawat gabi"),
    (124.09, "Wala mang nakikita"),
    (128.68, "Haplos mo'y ramdam pa rin sa dilim"),
    (133.13, "Hindi na nananaginip"),
    (137.84, "Hindi na ma- makagising"),
    (142.53, "Pasindi na ng ilaw"),
    (146.92, "Minumulto na 'ko ng damdamin ko (ng damdamin ko)"),
    (153.30, "'Di mo ba ako lilisanin?"),
    (157.21, "Hindi pa ba sapat pagpapahirap sa 'kin? (damdamin ko)"),
    (161.83, "Hindi na ba ma- mamamayapa?"),
    (166.77, "Hindi na ba ma- mamamayapa?"),
    (170.35, "Hindi na makalaya"),
    (174.93, "Dinadalaw mo 'ko bawat gabi"),
    (179.32, "Wala mang nakikita"),
    (183.99, "Haplos mo'y ramdam pa rin sa dilim"),
    (188.70, "Hindi na nananaginip"),
    (193.11, "Hindi na ma- makagising"),
    (197.63, "Pasindi na ng ilaw"),
    (202.47, "Minumulto na 'ko ng damdamin ko (ng damdamin ko)"),
    (208.37, "(Makalaya) hindi mo ba ako lilisanin?"),
    (212.10, "(Dinadalaw mo 'ko bawat gabi)"),
    (213.32, "Hindi pa ba sapat pagpapahirap sa 'kin? (Wala mang nakikita)"),
    (217.89, "Hindi na ba ma- mamamayapa? (Haplos mo'y ramdam pa rin sa dilim)"),
    (222.28, "Hindi na ba ma- mamamayapa?"),
    (227.28, "Thank you for watching!"),
    (232.28, "Like ^_^ and Follow :) for more!"),
]

# File paths
MUSIC_PATH = r"D:\PYTHON - Songs\mp3\Multo.mp3"
BG_IMAGE_PATH = r"D:\PYTHON - Songs\bg\bgq.jpg"

# Initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1000, 300), pygame.RESIZABLE)
pygame.display.set_caption("Multo - Cup of Joe")

# Fonts and colors
font = pygame.font.SysFont("Arial", 32)
TEXT_COLOR = (255, 255, 255)
CHAR_DELAY = 0.05
OVERLAY_ALPHA = 190

# Load background image
if os.path.exists(BG_IMAGE_PATH):
    background_raw = pygame.image.load(BG_IMAGE_PATH).convert()
else:
    raise FileNotFoundError("Background image not found at specified path.")

def draw_overlay(surface, alpha=240):
    overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, alpha))
    surface.blit(overlay, (0, 0))

def draw_wave_text_centered(surface, text, start_time, current_time):
    elapsed = current_time - start_time
    amplitude = 12
    y_base = surface.get_height() // 2

    # Word wrap
    words = text.split()
    lines = []
    line = ""
    max_width = surface.get_width() * 0.9  # 90% width

    for word in words:
        test_line = line + " " + word if line else word
        test_width = font.size(test_line)[0]
        if test_width <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)

    total_height = len(lines) * font.get_height()
    y = y_base - total_height // 2

    for line_text in lines:
        x = (surface.get_width() - font.size(line_text)[0]) // 2
        for i, char in enumerate(line_text):
            char_elapsed = elapsed - i * CHAR_DELAY
            if char_elapsed < 0:
                offset_y = 0
            elif char_elapsed < 0.3:
                offset_y = -math.sin(char_elapsed * math.pi / 0.3) * amplitude
            else:
                offset_y = 0
            char_surf = font.render(char, True, TEXT_COLOR)
            surface.blit(char_surf, (x, y + offset_y))
            x += char_surf.get_width()
        y += font.get_height()

def draw_play_button(surface):
    w, h = surface.get_size()
    center = (w // 2, h // 2)
    size = 40
    points = [
        (center[0] - size // 2, center[1] - size),
        (center[0] - size // 2, center[1] + size),
        (center[0] + size, center[1])
    ]
    pygame.draw.polygon(surface, TEXT_COLOR, points)

    return pygame.Rect(center[0] - size // 2, center[1] - size, size + size // 2, size * 2)

def wait_for_play_button():
    global screen
    global play_button_rect
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    return

        window_width, window_height = screen.get_size()
        bg_scaled = pygame.transform.smoothscale(background_raw, (window_width, window_height))
        screen.blit(bg_scaled, (0, 0))
        draw_overlay(screen, OVERLAY_ALPHA)
        play_button_rect = draw_play_button(screen)
        pygame.display.flip()
        clock.tick(60)

def play_music():
    pygame.mixer.music.load(MUSIC_PATH)
    pygame.mixer.music.play()

def sync_lyrics():
    global screen
    start_time = time.time()
    lyric_index = 0
    clock = pygame.time.Clock()
    running = True

    while running and lyric_index < len(lyrics):
        current_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.mixer.music.stop()
                return
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        timestamp, line = lyrics[lyric_index]
        if current_time >= timestamp:
            next_timestamp = lyrics[lyric_index + 1][0] if lyric_index + 1 < len(lyrics) else timestamp + 5
            line_start_time = time.time()
            while time.time() - start_time < next_timestamp and running:
                now = time.time()
                window_width, window_height = screen.get_size()
                bg_scaled = pygame.transform.smoothscale(background_raw, (window_width, window_height))
                screen.blit(bg_scaled, (0, 0))
                draw_overlay(screen, OVERLAY_ALPHA)
                draw_wave_text_centered(screen, line, line_start_time, now)
                pygame.display.flip()
                clock.tick(60)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.mixer.music.stop()
                        return
                    elif event.type == pygame.VIDEORESIZE:
                        screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            lyric_index += 1
        else:
            window_width, window_height = screen.get_size()
            bg_scaled = pygame.transform.smoothscale(background_raw, (window_width, window_height))
            screen.blit(bg_scaled, (0, 0))
            draw_overlay(screen, OVERLAY_ALPHA)
            pygame.display.flip()
            clock.tick(60)

def main():
    wait_for_play_button()
    threading.Thread(target=play_music).start()
    sync_lyrics()
    pygame.quit()

if __name__ == "__main__":
    main()