from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "segredo123"

usuarios = {}

# =========================
# CATÁLOGOS
# =========================
catalogos = {
    "cerveja": [
        {"id": "cerveja_1", "nome": "Cerveja Pilsen", "preco": 8.0,
         "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6F11-by6kKFK0ptBk66-Q3ODEYRrr7aefaQ&s"}
    ],
    "vinho": [
        {"id": "vinho_1", "nome": "Vinho Tinto", "preco": 45.0,
         "img": "https://www.viavini.com.br/blog-de-vinhos/wp-content/uploads/2020/08/h4-vinhos-velho-mundo-e-novo-mundo-viavini-exclusivos-1024x559.jpg"}
    ],
    "suco": [
        {"id": "suco_1", "nome": "Suco Natural", "preco": 25.0,
         "img": "https://saude.abril.com.br/wp-content/uploads/2018/11/destaque-tial-pagina.jpg"}
    ],
    "refri": [
        {"id": "refri_1", "nome": "Refrigerante", "preco": 6.0,
         "img": "https://io.convertiez.com.br/m/superpaguemenos/shop/products/images/55192/medium/kit-refrigerantes-coca-cola-fanta-kuat-e-sprite-2l_103103.jpg"}
    ]
}

# =========================
# LOGIN
# =========================
@app.route('/')
def login():
    return render_template("login.html")


@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    email = request.form.get('email')
    senha = request.form.get('password')

    if email in usuarios:
        return render_template("cadastro.html", erro="Usuário já existe")

    usuarios[email] = senha
    return redirect(url_for('login'))


@app.route('/logar', methods=['POST'])
def logar():
    email = request.form.get('email')
    senha = request.form.get('password')

    if email in usuarios and usuarios[email] == senha:
        session['logado'] = True
        session['carrinho'] = {}
        return redirect(url_for('home'))

    return render_template("login.html", erro="Login inválido")


# =========================
# HOME
# =========================
@app.route('/home')
def home():
    if not session.get('logado'):
        return redirect(url_for('login'))

    return render_template("index.html")


# =========================
# CATÁLOGO
# =========================
@app.route('/catalogo/<categoria>')
def catalogo(categoria):
    if not session.get('logado'):
        return redirect(url_for('login'))

    return render_template("catalogo.html", produtos=catalogos.get(categoria, []))


# =========================
# ADICIONAR AO CARRINHO
# =========================
@app.route('/add/<id>/<nome>/<float:preco>')
def add(id, nome, preco):

    carrinho = session.get('carrinho', {})

    # 🔥 GARANTE FORMATO CORRETO SEMPRE
    if not isinstance(carrinho, dict):
        carrinho = {}

    if id in carrinho:
        carrinho[id]["qtd"] += 1
    else:
        carrinho[id] = {
            "nome": nome,
            "preco": float(preco),
            "qtd": 1
        }

    session['carrinho'] = carrinho
    return redirect(url_for('carrinho'))


# =========================
# CARRINHO (PROTEGIDO 100%)
# =========================
@app.route('/carrinho')
def carrinho():

    carrinho = session.get('carrinho', {})

    if not isinstance(carrinho, dict):
        carrinho = {}

    itens = []
    total = 0

    for id, item in carrinho.items():

        # 🔥 EVITA ERRO INT
        if not isinstance(item, dict):
            continue

        subtotal = item["preco"] * item["qtd"]
        total += subtotal

        itens.append({
            "id": id,
            "nome": item["nome"],
            "preco": item["preco"],
            "qtd": item["qtd"],
            "subtotal": subtotal
        })

    return render_template("carrinho.html", itens=itens, total=total)


# =========================
# +1 ITEM
# =========================
@app.route('/add_one/<id>')
def add_one(id):

    carrinho = session.get('carrinho', {})

    if isinstance(carrinho, dict) and id in carrinho:
        carrinho[id]["qtd"] += 1

    session['carrinho'] = carrinho
    return redirect(url_for('carrinho'))


# =========================
# -1 ITEM
# =========================
@app.route('/remove_one/<id>')
def remove_one(id):

    carrinho = session.get('carrinho', {})

    if isinstance(carrinho, dict) and id in carrinho:
        carrinho[id]["qtd"] -= 1

        if carrinho[id]["qtd"] <= 0:
            del carrinho[id]

    session['carrinho'] = carrinho
    return redirect(url_for('carrinho'))


# =========================
# FINALIZAR COMPRA
# =========================
@app.route('/finalizar')
def finalizar():
    session['carrinho'] = {}
    return render_template("checkout.html")


# =========================
# RESET (REMOVE BUG ANTIGO)
# =========================
@app.route('/reset')
def reset():
    session.clear()
    return "sessão limpa"


# =========================
# LOGOUT
# =========================
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)