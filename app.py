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
        "pa
