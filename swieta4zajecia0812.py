import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# --- Konfiguracja i stałe ---

# Kolory
KOLOR_CZAPKA_DOMYSLNY = 'red'
KOLOR_CZAPKA_ZMIANA = 'blue'
KOLOR_BRODA = '#f5f5dc'        # Kolor brody (jasny beż/śmietankowy)
KOLOR_TWARZ = '#ffe0bd'        # Kolor skóry
KOLOR_OCZY = 'black'
KOLOR_POMPON_FUTERKO = 'white' # Kolor futerka/pomponu/brody
KOLOR_KOMBINEZON = 'red'       # Kolor ubrania
KOLOR_BUTY_REKAWICE = 'black'  # Kolor butów i rękawic

# Nazwa zmiennej stanu do przechowywania koloru czapki
STAN_KOLOR_CZAPKI = 'kolor_czapki'


def stworz_mikolaja(kolor_czapki):
    """
    Tworzy i zwraca obiekt Matplotlib Figure (Mikołaja) z rozszerzonym ciałem.
    """
    fig, ax = plt.subplots(figsize=(6, 10))
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-2.0, 1.2)
    ax.axis('off')  # Ukryj osie

    # --- Rysowanie Ciała ---
    # Brzuch/Tułów (duże koło)
    brzuch = patches.Circle((0, -0.7), 0.7, facecolor=KOLOR_KOMBINEZON, zorder=1)
    ax.add_patch(brzuch)
    
    # Pas (prostokąt)
    pas = patches.Rectangle((-0.7, -0.95), 1.4, 0.1, facecolor='brown', zorder=2)
    ax.add_patch(pas)
    
    # Klamra pasa (kwadrat)
    klamra = patches.Rectangle((-0.15, -0.95), 0.3, 0.1, facecolor='gold', zorder=3)
    ax.add_patch(klamra)

    # Nogi (prostokąty)
    noga_lewa = patches.Rectangle((-0.4, -1.8), 0.3, 0.85, facecolor=KOLOR_KOMBINEZON, zorder=1)
    noga_prawa = patches.Rectangle((0.1, -1.8), 0.3, 0.85, facecolor=KOLOR_KOMBINEZON, zorder=1)
    ax.add_patch(noga_lewa)
    ax.add_patch(noga_prawa)

    # Buty (zaokrąglone prostokąty lub elipsy)
    but_lewy = patches.Ellipse((-0.25, -1.8), 0.5, 0.2, angle=0, facecolor=KOLOR_BUTY_REKAWICE, zorder=4)
    but_prawy = patches.Ellipse((0.25, -1.8), 0.5, 0.2, angle=0, facecolor=KOLOR_BUTY_REKAWICE, zorder=4)
    ax.add_patch(but_lewy)
    ax.add_patch(but_prawy)
    
    # Ręce (prostokąty)
    ramie_lewe = patches.Rectangle((-1.2, -0.8), 0.8, 0.2, angle=-20, facecolor=KOLOR_KOMBINEZON, zorder=1)
    ramie_prawe = patches.Rectangle((0.4, -0.8), 0.8, 0.2, angle=20, facecolor=KOLOR_KOMBINEZON, zorder=1)
    ax.add_patch(ramie_lewe)
    ax.add_patch(ramie_prawe)
    
    # Rękawice (koła)
    rekawica_lewa = patches.Circle((-1.35, -1.0), 0.15, facecolor=KOLOR_BUTY_REKAWICE, zorder=4)
    rekawica_prawa = patches.Circle((1.35, -1.0), 0.15, facecolor=KOLOR_BUTY_REKAWICE, zorder=4)
    ax.add_patch(rekawica_lewa)
    ax.add_patch(rekawica_prawa)


    # --- Rysowanie Głowy ---

    # Twarz (koło)
    twarz = patches.Circle((0, 0), 0.4, facecolor=KOLOR_TWARZ, zorder=5)
    ax.add_patch(twarz)

    # Broda (Duży półokrąg pod twarzą) - Zmieniona, aby była bardziej wyrazista
    broda = patches.Arc((0, 0), 1.0, 1.0, angle=0, theta1=200, theta2=340, 
                        facecolor=KOLOR_POMPON_FUTERKO, edgecolor=KOLOR_POMPON_FUTERKO, linewidth=1, zorder=6)
    ax.add_patch(broda)
    
    # Wąsy (poprawione)
    wasy_lewy = patches.Rectangle((-0.4, -0.1), 0.25, 0.08, angle=5, color=KOLOR_POMPON_FUTERKO, zorder=7)
    wasy_prawy = patches.Rectangle((0.15, -0.1), 0.25, 0.08, angle=-5, color=KOLOR_POMPON_FUTERKO, zorder=7)
    ax.add_patch(wasy_lewy)
    ax.add_patch(wasy_prawy)

    # Usta/nos (mały czerwony nosek)
    nos = patches.Circle((0, 0), 0.05, facecolor='red', zorder=8)
    ax.add_patch(nos)
    
    # Oczy
    oko_lewe = patches.Circle((-0.15, 0.15), 0.05, facecolor=KOLOR_OCZY, zorder=8)
    oko_prawe = patches.Circle((0.15, 0.15), 0.05, facecolor=KOLOR_OCZY, zorder=8)
    ax.add_patch(oko_lewe)
    ax.add_patch(oko_prawe)

    # Czapka (trójkąt) - Używamy przekazanego koloru
    czapka_wierzcholki = np.array([
        [-0.45, 0.3],
        [0.45, 0.3],
        [0, 1.0]
    ])
    czapka_patch = patches.Polygon(czapka_wierzcholki, closed=True, facecolor=kolor_czapki, zorder=9)
    ax.add_patch(czapka_patch)

    # Futerko/Obręcz czapki
    futerko = patches.Rectangle((-0.5, 0.25), 1.0, 0.1, facecolor=KOLOR_POMPON_FUTERKO, zorder=10)
    ax.add_patch(futerko)

    # Pompon
    pompon = patches.Circle((0, 1.0), 0.1, facecolor=KOLOR_POMPON_FUTERKO, zorder=11)
    ax.add_patch(pompon)

    plt.title("Wesołych Świąt! Kolor czapki: {}".format(kolor_czapki.upper()))

    return fig


def zmien_kolor():
    """
    Funkcja zmieniająca kolor czapki w stanie Streamlit.
    """
    obecny_kolor = st.session_state[STAN_KOLOR_CZAPKI]
    if obecny_kolor == KOLOR_CZAPKA_DOMYSLNY:
        nowy_kolor = KOLOR_CZAPKA_ZMIANA
    else:
        nowy_kolor = KOLOR_CZAPKA_DOMYSLNY

    st.session_state[STAN_KOLOR_CZAPKI] = nowy_kolor


def main():
    st.set_page_config(page_title="Interaktywny Mikołaj", layout="centered")
    st.title("Interaktywny Mikołaj w Streamlit 🧑‍🎄")
    st.markdown("Kliknij przycisk, aby zmienić kolor czapki! Teraz Mikołaj ma **brzuch**, **ręce**, **nogi** i ładniejszą **brodę**.")

    # 1. Inicjalizacja stanu (Session State)
    if STAN_KOLOR_CZAPKI not in st.session_state:
        st.session_state[STAN_KOLOR_CZAPKI] = KOLOR_CZAPKA_DOMYSLNY

    # 2. Przycisk
    st.button(
        "Zmień Kolor Czapki!",
        on_click=zmien_kolor
    )

    st.write("---")

    # 3. Rysowanie Mikołaja
    aktualny_kolor = st.session_state[STAN_KOLOR_CZAPKI]
    mikolaj_fig = stworz_mikolaja(aktualny_kolor)
    
    # Wyświetl figurę w Streamlit
    st.pyplot(mikolaj_fig)


if __name__ == '__main__':
    main()
