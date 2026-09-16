import os
import random
import flet as ft

def main(page: ft.Page):
    page.title = "𝔐𝔎-Flix"
    page.bgcolor = "#141414"  # Fundo escuro estilo Netflix
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    # 🎬 CATALOGO DE FILMES E SÉRIES Privados (Substitua pelos seus links .mp4 reais)
    videos = [
        {
            "titulo": "Filme Privado 1", 
            "url": "https://googleapis.com",
            "desc": "Toque para reproduzir o seu primeiro filme no player nativo."
        },
        {
            "titulo": "Série Exemplo - Ep 01", 
            "url": "https://googleapis.com",
            "desc": "Primeiro episódio da sua série privada."
        },
        {
            "titulo": "Filme Privado 2", 
            "url": "https://googleapis.com",
            "desc": "Mais um vídeo configurado no seu catálogo pessoal."
        }
    ]

    # Barra superior com o seu nome
    topo = ft.Row(
        controls=[
            ft.Text("𝔐𝔎𝔠𝔩𝔞𝔲𝔡𝔦𝔦𝔫", size=18, weight=ft.FontWeight.BOLD, color="#E50914"),
            ft.Text("🍿 MEU CINEMA PRIVADO", size=14, weight=ft.FontWeight.W_500, color="white")
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    grade_filmes = ft.Column(spacing=15)
    
    for v in videos:
        card = ft.Container(
            content=ft.Column([
                ft.Text(v["titulo"], size=18, weight=ft.FontWeight.BOLD, color="white"),
                ft.Text(v["desc"], size=13, color="#AAAAAA"),
                ft.Container(height=5),
                ft.FilledButton(
                    "Assistir Agora 🍿", 
                    bgcolor="#E50914", 
                    color="white",
                    on_click=lambda e, url=v["url"]: page.open(url)
                )
            ]),
            bgcolor="#1F1F1F",
            padding=20,
            border_radius=15,
            width=360,
            shadow=ft.BoxShadow(blur_radius=10, color="rgba(0,0,0,0.5)")
        )
        grade_filmes.controls.append(card)

    page.add(
        ft.Container(
            content=ft.Column([
                topo,
                ft.Divider(color="#333333"),
                ft.Container(height=10),
                ft.Text("Filmes e Séries Disponíveis:", size=16, weight=ft.FontWeight.BOLD, color="white"),
                ft.Container(height=5),
                grade_filmes
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            width=380,
            padding=20
        )
    )

if __name__ == "__main__":
    ft.run(main)
