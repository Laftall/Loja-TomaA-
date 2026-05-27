from flask import Flask, render_template, request, redirect, url_for, session, make_response

app = Flask(__name__)
app.secret_key = "segredo123"

usuarios = {}

# CATÁLOGOS

catalogos = {
    "cerveja": [
        {
            "id": "cerveja_1",
            "nome": "Skol 600ml",
            "preco": "8.00",
            "img": "https://imagens.jotaja.com/produtos/9d1527a0-7802-47dc-8ed8-8c0f9fdd9feb.jpg"
        },
        {
            "id": "cerveja_2",
            "nome": "Original 600ml",
            "preco": "9.50",
            "img": "https://emporiodacerveja.vteximg.com.br/arquivos/ids/163420-1000-1000/03.jpg"
        },
        {
            "id": "cerveja_3",
            "nome": "Budweiser 600ml",
            "preco": "10.00",
            "img": "https://emporiodacerveja.vteximg.com.br/arquivos/ids/161884-1000-1000/imagebud.jpg"
        },
        {
            "id": "cerveja_4",
            "nome": "Spaten 600ml",
            "preco": "12.50",
            "img": "https://redemix.vteximg.com.br/arquivos/ids/211638-1000-1000/7891991297547.jpg?v=638350615048070000"
        },
        {
            "id": "cerveja_5",
            "nome": "Stella Artois 600ml",
            "preco": "12.00",
            "img": "https://m.media-amazon.com/images/I/71l0hKnNtaL._AC_UF1000,1000_QL80_.jpg"
        },
        {
            "id": "cerveja_6",
            "nome": "Brahma 600ml",
            "preco": "8.00",
            "img": "https://acdn-us.mitiendanube.com/stores/001/043/122/products/273_secundario-8ad58806d51cd37d4a17745577400560-1024-1024.webp"
        },
        {
            "id": "cerveja_7",
            "nome": "Corona 600ml",
            "preco": "10.00",
            "img": "https://cdn.vucasolution.com.br/upload/w_800/https://gryyplgyeyqb.compat.objectstorage.sa-saopaulo-1.oraclecloud.com/vuca-cdn/botecosabia/arqs/produtos/dlermpspkbxy2qdbudnq.jpg"
        }
    ],

    "vinho": [
        {
            "id": "vinho_1",
            "nome": "Tinto suave",
            "preco": "45.00",
            "img": "https://carrefourbrfood.vtexassets.com/arquivos/ids/61611723/vho-tto-chi-c-diablo-rsv-red-blend-750ml-1.jpg?v=637913550618900000"
        },
        {
            "id": "vinho_2",
            "nome": "Tinto seco",
            "preco": "42.00",
            "img": "https://supermercadobomdemais.com.br/wp-content/uploads/2020/06/Vinho-Casillero-del-Diablo-Merlot.jpg"
        },
        {
            "id": "vinho_3",
            "nome": "Branco suave",
            "preco": "40.00",
            "img": "https://cdn.dooca.store/1390/products/prancheta-1-copiar-2.png?v=1675793574000"
        },
        {
            "id": "vinho_4",
            "nome": "Branco seco",
            "preco": "38.00",
            "img": "https://cdn-cosmos.bluesoft.com.br/products/7804320750354"
        },
        {
            "id": "vinho_5",
            "nome": "Rosé",
            "preco": "60.00",
            "img": "https://phygital-files.mercafacil.com/catalogo/uploads/produto/vinho_chileno_casillero_del_diablo_ros_750ml_61dbd0f8-bf4a-4469-b9e8-0e58f094421a.jpg"
        }
    ],

    "suco": [
        {
            "id": "suco_1",
            "nome": "Suco Laranja 1L",
            "preco": "9.90",
            "img": "https://carrefourbrfood.vtexassets.com/arquivos/ids/24027989/4308956_1.jpg?v=637692175902400000"
        },
        {
            "id": "suco_2",
            "nome": "Suco Uva 1L",
            "preco": "10.90",
            "img": "https://andinacocacola.vtexassets.com/arquivos/ids/158632/Del-Valle-Nectar-Uva-1L-114644_COCA.jpg?v=639094449089730000"
        },
        {
            "id": "suco_3",
            "nome": "Suco Pêssego 1L",
            "preco": "10.90",
            "img": "https://andinacocacola.vtexassets.com/arquivos/ids/158633/Del-Valle-Nectar-Pessego-1L-114574_COCA_1.jpg?v=639094449089670000"
        },
        {
            "id": "suco_4",
            "nome": "Suco Maçã 1L",
            "preco": "11.90",
            "img": "https://andinacocacola.vtexassets.com/arquivos/ids/158224/DV-MACA--114472_COCA-.jpg?v=639094449081900000"
        },
        {
            "id": "suco_5",
            "nome": "Suco Maracujá 1L",
            "preco": "12.90",
            "img": "https://andinacocacola.vtexassets.com/arquivos/ids/158631/Del-Valle-Nectar-Maracuja-1L-114580_COCA_1.jpg?v=639094449089800000"
        },
        {
            "id": "suco_6",
            "nome": "Suco Abacaxi 1L",
            "preco": "12.90",
            "img": "https://andinacocacola.vtexassets.com/arquivos/ids/158626/Del-Valle-Nectar-Abacaxi-1L-114647_COCA_1.jpg?v=639094449082230000"
        },
        {
            "id": "suco_7",
            "nome": "Suco Caju 1L",
            "preco": "9.90",
            "img": "https://mambodelivery.vtexassets.com/arquivos/ids/222141/150555-Suco-de-Caju-sem-Acucar-Del-Valle-1L.jpg?v=638652814499270000"
        }
    ],

    "refri": [
        {
            "id": "refri_1",
            "nome": "Coca-Cola 1L",
            "preco": "8.50",
            "img": "https://d3gdr9n5lqb5z7.cloudfront.net/fotos/intellibrand_000000000000986231-LT_2.jpg"
        },
        {
            "id": "refri_2",
            "nome": "Pepsi 1L",
            "preco": "8.00",
            "img": "https://rimibaltic-res.cloudinary.com/image/upload/b_white,c_limit,dpr_auto,f_auto,q_auto:low,w_auto/d_ecommerce:backend-fallback.png/MAT_1360359_PCE_LT"
        },
        {
            "id": "refri_3",
            "nome": "Kuat 1L",
            "preco": "7.50",
            "img": "https://redemix.vteximg.com.br/arquivos/ids/216203-1000-1000/7894900911756.jpg?v=638424803544500000"
        },
        {
            "id": "refri_4",
            "nome": "Sprite 1L",
            "preco": "8.00",
            "img": "https://carrefourbrfood.vtexassets.com/arquivos/ids/62338329/refrigerante-sprite-limao-original-pt-1l-1.jpg?v=637915896816630000"
        },
        {
            "id": "refri_5",
            "nome": "Guaraná 1L",
            "preco": "8.00",
            "img": "https://d3gdr9n5lqb5z7.cloudfront.net/fotos/977469-2-16-09-2025-17-21-49-564.jpg"
        },
        {
            "id": "refri_6",
            "nome": "Coca-Cola Zero 1L",
            "preco": "9.00",
            "img": "https://redemix.vteximg.com.br/arquivos/ids/211999-1000-1000/7894900701715.jpg?v=638350616469630000"
        },
        {
            "id": "refri_7",
            "nome": "Fanta Laranja 1L",
            "preco": "6.00",
            "img": "https://d3gdr9n5lqb5z7.cloudfront.net/fotos/7894900031751-14-11-2025-16-04-04-31.jpg"
        },
        {
            "id": "refri_8",
            "nome": "Fanta Uva 1L",
            "preco": "6.00",
            "img": "https://andinacocacola.vtexassets.com/arquivos/ids/159006/Fanta-Uva-15L-Pet--110427_COCA-.jpg?v=639094449080970000"
        }
    ],
    "agua": [
        {
            "id": "agua_1",
            "nome": "Água Sem Gás 1L",
            "preco": "4.00",
            "img": "https://drogariaspacheco.vteximg.com.br/arquivos/ids/745445-1000-1000/706647---agua-crystal-sem-gas-1-5l.jpg?v=637787362090000000"
        },
        {
            "id": "agua_2",
            "nome": "Água com Gás 1L",
            "preco": "4.50",
            "img": "https://carrefourbrfood.vtexassets.com/arquivos/ids/18904681/agua-mineral-com-gas-crystal-15-litros-1.jpg?v=637590230893170000"
        },
        {
            "id": "agua_3",
            "nome": "Água sem Gás 500ml",
            "preco": "2.50",
            "img": "https://product-data.raiadrogasil.io/images/3448200.webp"
        },
        {
            "id": "agua_4",
            "nome": "Água com Gás 500ml",
            "preco": "2.90",
            "img": "https://d3gdr9n5lqb5z7.cloudfront.net/fotos/983651-17-02-2023-17-00-15-288.jpg"
        }
    ]
    
}

# FUNÇÃO ANTI CACHE

def no_cache(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# LOGIN

@app.route('/')
def login():
    response = make_response(render_template("login.html"))
    return no_cache(response)

# CADASTRO

@app.route('/cadastro')
def cadastro():
    response = make_response(render_template("cadastro.html"))
    return no_cache(response)

# CADASTRAR

@app.route('/cadastrar', methods=['POST'])
def cadastrar():

    email = request.form.get('email')
    senha = request.form.get('password')

    usuarios[email] = senha

    return redirect(url_for('login'))

# LOGAR

@app.route('/logar', methods=['POST'])
def logar():

    email = request.form.get('email')
    senha = request.form.get('password')

    if email in usuarios and usuarios[email] == senha:

        session['logado'] = True
        session['carrinho'] = {}

        return redirect(url_for('home'))

    return render_template(
        "login.html",
        erro="Email ou senha inválidos"
    )

# HOME

@app.route('/home')
def home():

    if not session.get('logado'):
        return redirect(url_for('login'))

    response = make_response(render_template("index.html"))
    return no_cache(response)

# CATÁLOGO

@app.route('/catalogo/<categoria>')
def catalogo(categoria):

    if not session.get('logado'):
        return redirect(url_for('login'))

    response = make_response(
        render_template(
            "catalogo.html",
            produtos=catalogos.get(categoria, []),
            categoria=categoria
        )
    )

    return no_cache(response)

# ADICIONAR AO CARRINHO

@app.route('/add/<id>/<nome>/<float:preco>/<path:img>')
def add(id, nome, preco, img):

    if not session.get('logado'):
        return redirect(url_for('login'))

    carrinho = session.get('carrinho', {})

    if id in carrinho:
        carrinho[id]["qtd"] += 1
    else:
        carrinho[id] = {
            "nome": nome,
            "preco": preco,
            "img": img,
            "qtd": 1
        }

    session['carrinho'] = carrinho

    return redirect(url_for('carrinho'))

# CARRINHO

@app.route('/carrinho')
def carrinho():

    if not session.get('logado'):
        return redirect(url_for('login'))

    carrinho = session.get('carrinho', {})

    itens = []
    total = 0

    for id, item in carrinho.items():

        if not isinstance(item, dict):
            continue

        subtotal = item["preco"] * item["qtd"]
        total += subtotal

        itens.append({
            "id": id,
            "nome": item["nome"],
            "preco": item["preco"],
            "img": item["img"],
            "qtd": item["qtd"],
            "subtotal": subtotal
        })

    response = make_response(
        render_template(
            "carrinho.html",
            itens=itens,
            total=total
        )
    )

    return no_cache(response)

# +1 ITEM

@app.route('/add_one/<id>')
def add_one(id):

    if not session.get('logado'):
        return redirect(url_for('login'))

    carrinho = session.get('carrinho', {})

    if id in carrinho:
        carrinho[id]["qtd"] += 1

    session['carrinho'] = carrinho

    return redirect(url_for('carrinho'))

# -1 ITEM

@app.route('/remove_one/<id>')
def remove_one(id):

    if not session.get('logado'):
        return redirect(url_for('login'))

    carrinho = session.get('carrinho', {})

    if id in carrinho:

        carrinho[id]["qtd"] -= 1

        if carrinho[id]["qtd"] <= 0:
            del carrinho[id]

    session['carrinho'] = carrinho

    return redirect(url_for('carrinho'))

# LIMPAR CARRINHO

@app.route('/limpar_carrinho')
def limpar_carrinho():

    if not session.get('logado'):
        return redirect(url_for('login'))

    session['carrinho'] = {}

    return redirect(url_for('carrinho'))

# FINALIZAR

@app.route('/finalizar')
def finalizar():

    if not session.get('logado'):
        return redirect(url_for('login'))

    session['carrinho'] = {}

    response = make_response(render_template("checkout.html"))
    return no_cache(response)

# LOGOUT

@app.route('/logout')
def logout():

    session.clear()

    response = redirect(url_for('login'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response

# START SERVER

if __name__ == "__main__":
    app.run(debug=True)