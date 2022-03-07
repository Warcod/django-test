from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    return HttpResponse("Hola, soy la pagina de inicio")

def otra_vista(request):
    
    return HttpResponse("""
                        !DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="/Users/guidoirigoyen/Documents/Js-Dalto/web/style.css">
	<style>@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');</style>
	<title>Bienvenidos a mi web</title>
</head>
<body class="body">
	<header class="top_header">
		<img src="/Users/guidoirigoyen/Documents/Js-Dalto/web/images/logo.svg" width="200px" height="100px" class="logo">
		<nav>
			<a href="/Users/guidoirigoyen/Documents/Js-Dalto/web/main.html" class="links">Inicio</a>
			<a href="/Users/guidoirigoyen/Documents/Js-Dalto/web/sobremi.html" class="links">Sobre mi</a>
			<a href="/Users/guidoirigoyen/Documents/Js-Dalto/web/blog.html" class="links">Blog</a>
			<button class="button"><a href="/Users/guidoirigoyen/Documents/Js-Dalto/web/contacto.html" class="links">Contacto</a></button>
		</nav>
	</header>

	<main class="main">
		<section>
			<div class="cuerpo">
				<h1 class="titulo1">Bienvenidos a mi web, esto es solo una parte de mi</h1><br>

				<iframe width="560" height="315" src="https://www.youtube.com/embed/zY4xz9UdMZo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

				<p class="parrafo">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p><br>

				<h2 class="titulo2">Bienvenidos a mi web, esto es solo una parte de mi</h2><br>

				<img src="">

				<p class="parrafo">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p><br>

			</div>
		</section>
	</main>	

</body>
<footer class="footer">
	<p>Copywhrite</p>
	<a class="links" href="/Users/guidoirigoyen/Documents/Js-Dalto/web/main.html">Inicio</a>
</footer>
</html>
                        """)
    
def clase(request):
    return render(request, )