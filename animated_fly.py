import time
import math

PLANE = [
    r"       __|__       ",
    r" --@--@--(_)--@--@--  ",
]

def clear_screen_safe():
    """Tyhjentää näytön tulostamalla paljon tyhjää."""
    print("\n" * 100)

def draw_frame(x_offset, sky_padding):
    pad_x = " " * x_offset
    plane = "\n".join(pad_x + line for line in PLANE)
    # lisätään "taivasta" koneen alle -> näyttää siltä että kone on korkealla
    sky = "\n" * sky_padding
    return plane + sky

def animate_takeoff(fps=20):
    width = 35      # lentomatka
    sky_max = 0     # alkuperäinen korkeus (maata lähellä)
    sky_min = 15    # paljon taivasta koneen alle -> näyttää korkeammalta

    try:
        for x in range(width):
            # eteneminen 0..1
            progress = x / width
            # mitä pidemmälle mennään, sitä enemmän "taivasta" koneen alle
            sky_padding = int(sky_max + progress * (sky_min - sky_max))

            # pieni aaltoiluefekti lisäksi
            wave = int(1.5 * math.sin(x * 0.3))
            sky_padding += wave

            clear_screen_safe()
            print(draw_frame(x, sky_padding))
            time.sleep(1 / fps)

        clear_screen_safe()
    except KeyboardInterrupt:
        clear_screen_safe()

if __name__ == "__main__":
    time.sleep(1)
    animate_takeoff()
