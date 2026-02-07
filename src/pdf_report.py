

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_model_report(metrics, save_path="reports/model_report.pdf"):
    os.makedirs("reports", exist_ok=True)

    c = canvas.Canvas(save_path, pagesize=A4)
    width, height = A4

    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Fake Job Detection – Model Performance Report")

    y -= 40
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Generated On: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

    y -= 40
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Performance Metrics")

    y -= 30
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Accuracy : {metrics['accuracy'] * 100:.2f}%")
    y -= 20
    c.drawString(50, y, f"Precision: {metrics['precision'] * 100:.2f}%")
    y -= 20
    c.drawString(50, y, f"Recall   : {metrics['recall'] * 100:.2f}%")
    y -= 20
    c.drawString(50, y, f"F1 Score : {metrics['f1'] * 100:.2f}%")

    y -= 40
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Confusion Matrix")

    y -= 30
    c.setFont("Helvetica", 11)
    cm = metrics["confusion_matrix"]
    c.drawString(50, y, f"True Negative : {cm[0][0]}")
    y -= 20
    c.drawString(50, y, f"False Positive: {cm[0][1]}")
    y -= 20
    c.drawString(50, y, f"False Negative: {cm[1][0]}")
    y -= 20
    c.drawString(50, y, f"True Positive : {cm[1][1]}")

    c.showPage()
    c.save()

    return save_path
