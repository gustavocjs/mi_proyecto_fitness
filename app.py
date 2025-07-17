from flask import Flask, render_template, abort, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'una_clave_secreta'  # Necesario para los mensajes flash

planes = [
    {
        "id": "basico",
        "nombre": "Plan Básico",
        "precio": "$10 USD",
        "descripcion": "Acceso a rutinas básicas y consejos nutricionales.",
        "detalle": "Este plan incluye rutinas para principiantes, seguimiento básico y soporte vía email.",
        "pagos": "Transferencia bancaria, MercadoPago, PayPal."
    },
    {
        "id": "intermedio",
        "nombre": "Plan Intermedio",
        "precio": "$25 USD",
        "descripcion": "Incluye rutinas intermedias, planes de comida y contacto vía email.",
        "detalle": "Plan con rutinas personalizadas, dietas detalladas y soporte vía email.",
        "pagos": "Transferencia bancaria, MercadoPago, PayPal."
    },
    {
        "id": "premium",
        "nombre": "Plan Premium",
        "precio": "$50 USD",
        "descripcion": "Rutinas avanzadas, dietas personalizadas y contacto directo por WhatsApp.",
        "detalle": "Plan completo con asesoría 24/7, rutinas avanzadas, y contacto directo por WhatsApp.",
        "pagos": "Transferencia bancaria, MercadoPago, PayPal."
    }
]

@app.route('/')
def home():
    return render_template("index.html", planes=planes)

@app.route('/plan/<plan_id>')
def plan_detail(plan_id):
    plan = next((p for p in planes if p['id'] == plan_id), None)
    if plan is None:
        abort(404)
    return render_template("plan.html", plan=plan)

@app.route('/contacto', methods=['POST'])
def contacto():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    mensaje = request.form.get('mensaje')
    print(f"Mensaje recibido de {nombre} ({email}): {mensaje}")
    flash('¡Gracias por tu mensaje! Te responderé pronto.')
    return redirect(url_for('home'))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
