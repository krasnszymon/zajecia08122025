import streamlit as st
from supabase import create_client, Client

# --- KONFIGURACJA POŁĄCZENIA ---
URL = "https://smxblirvwlgrezohkcyr.supabase.co"
KEY = "sb_publishable_ywKAKTzluGPE-5sU-bhsFQ_-8wQUxjv"

@st.cache_resource
def init_connection():
    return create_client(URL, KEY)

try:
    supabase = init_connection()
except Exception as e:
    st.error(f"Błąd połączenia: {e}")
    st.stop()

st.set_page_config(page_title="Wynajem Sprzętu Eventowego", layout="centered")
st.title("🎸 System Wynajmu Sprzętu")

# --- ZAKŁADKI ---
tab1, tab2, tab3 = st.tabs(["📋 Dodaj Sprzęt", "📁 Kategorie Sprzętu", "📊 Stan Magazynu"])

# --- KATEGORIE ---
with tab2:
    st.header("Nowa Grupa Sprzętowa")
    with st.form("event_category_form", clear_on_submit=True):
        kat_nazwa = st.text_input("Nazwa grupy (np. Multimedia, Meble)")
        kat_opis = st.text_area("Opis przeznaczenia")
        submit_kat = st.form_submit_button("Zarejestruj Grupę")

        if submit_kat:
            if kat_nazwa:
                try:
                    data = {"nazwa": kat_nazwa, "opis": kat_opis}
                    supabase.table("kategorie").insert(data).execute()
                    st.success(f"Grupa '{kat_nazwa}' została utworzona.")
                except Exception as e:
                    st.error(f"Błąd: {e}")
            else:
                st.error("Podaj nazwę grupy!")

# --- SPRZĘT (PRODUKTY) ---
with tab1:
    st.header("Dodaj Sprzęt do Wynajmu")
    
    try:
        categories_res = supabase.table("kategorie").select("id, nazwa").execute()
        categories_data = categories_res.data
    except Exception as e:
        st.error(f"Błąd pobierania grup: {e}")
        categories_data = []
    
    if not categories_data:
        st.warning("Najpierw zdefiniuj grupy sprzętowe w zakładce obok!")
    else:
        cat_options = {item['nazwa']: item['id'] for item in categories_data}
        
        with st.form("equipment_form", clear_on_submit=True):
            prod_nazwa = st.text_input("Nazwa urządzenia/przedmiotu")
            prod_liczba = st.number_input("Ilość dostępnych sztuk", min_value=1, step=1)
            prod_cena = st.number_input("Cena za dobę wynajmu (zł)", min_value=0.0, step=0.50, format="%.2f")
            prod_kat_nazwa = st.selectbox("Przypisz do grupy", options=list(cat_options.keys()))
            
            submit_prod = st.form_submit_button("Dodaj do Inwentarza")
            
            if submit_prod:
                if prod_nazwa:
                    try:
                        product_data = {
                            "nazwa": prod_nazwa,
                            "liczba": prod_liczba,
                            "cena": float(prod_cena),
                            "kategorie_id": cat_options[prod_kat_nazwa]
                        }
                        # Używamy Twojej tabeli "Produkty" jako inwentarza sprzętu
                        supabase.table("Produkty").insert(product_data).execute()
                        st.success(f"Sprzęt '{prod_nazwa}' jest gotowy do wynajmu.")
                    except Exception as e:
                        st.error(f"Błąd zapisu: {e}")
                else:
                    st.error("Nazwa sprzętu jest wymagana!")

# --- PODGLĄD ---
with tab3:
    st.header("Podgląd Magazynu")
    
    res_kat = supabase.table("kategorie").select("id, nazwa, opis").execute()
    res_prod = supabase.table("Produkty").select("id, nazwa, liczba, cena, kategorie_id").execute()
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Grupy")
        st.dataframe(res_kat.data, use_container_width=True)
    with c2:
        st.subheader("Inwentarz")
        st.dataframe(res_prod.data, use_container_width=True)
